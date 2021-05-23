import git
from django.shortcuts import render
from subprocess import Popen
import shlex
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
from pathlib import Path
import os

from django.views.decorators.http import require_POST
from rest_framework import status
from rest_framework.utils import json

logger = logging.getLogger(__name__)
BASE_DIR = Path(__file__).resolve().parent.parent


@csrf_exempt
@require_POST
def update(request):
    logger.info("#CICD received {},request : {} with headers: {}".format(request.method, request.body, request.headers))
    try:
        '''
                pass the path of the diectory where your project will be 
                stored on PythonAnywhere in the git.Repo() as parameter.
                '''
        request_payload = json.loads(request.body)
        logger.debug("#CICD Request body : {}".format(request_payload))
        if request_payload["action"] == "closed":
            pull_request = request_payload["pull_request"]
            if pull_request["merged"]:
                logger.debug("#CICD path : {}".format(BASE_DIR))
                repo = git.Repo(BASE_DIR)
                origin = repo.remotes.origin

                logger.info("#CICD updating project")
                origin.pull()
                logger.info("#CICD project updated successfully")

                update_requirements()

                return HttpResponse("Updated code on PythonAnywhere",
                                    status=status.HTTP_200_OK)
            else:
                logger.info("Received hook for closed with unmerged commits Pull request: {} ".format(pull_request))
                return HttpResponse("PR closed with unmerged commits webhook received on PythonAnywhere",
                                    status=status.HTTP_200_OK)
        else:
            logger.info("Received hook for not closed Pull request: {} ".format(request_payload))
            return HttpResponse("PR not closed webhook received on PythonAnywhere",
                                status=status.HTTP_200_OK)

    except ConnectionError as ex:
        logger.error("#CICD update connection error : {}".format(str(ex)))
        return HttpResponse("Connection error while for updating code on PythonAnyWhere",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except PermissionError as ex:
        logger.error("#CICD update Permission error : {}".format(str(ex)))
        return HttpResponse("Permission error while updating code on PythonAnyWhere",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except TimeoutError as ex:
        logger.error("#CICD update timed out : {}".format(str(ex)))
        return HttpResponse("Timed out while updating code on PythonAnyWhere",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except RuntimeError as ex:
        logger.error("#CICD Runtime error : {}".format(str(ex)))
        return HttpResponse("RuntimeError while updating code on PythonAnyWhere",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as ex:
        logger.error("#CICD global exception : {}".format(str(ex)))
        return HttpResponse("Exception occurred while updating code on PythonAnyWhere",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def update_requirements():
    env = os.getenv("VIRTUAL_ENV")
    logger.info("#CICD updating {} requirements".format(env))
    Popen(shlex.split(
        '/bin/bash -c "source {}/bin/activate && pip install -r {}/requirements.txt && python {}/manage.py '
        'collectstatic -y && python {}/manage.py migrate -y "'.format(env, BASE_DIR, BASE_DIR, BASE_DIR)))
    logger.info("#CICD requirements updated for {}".format(env))
