import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import logging
from pathlib import Path
import os

from django.views.decorators.http import require_POST

logger = logging.getLogger(__name__)
BASE_DIR = Path(__file__).resolve().parent.parent


@csrf_exempt
@require_POST
def update(request):
    logger.info("#CICD received {},request : {} with headers: {}".format(request.method, request.body, request.headers))
    if request.method == "POST":
        try:
            '''
                    pass the path of the diectory where your project will be 
                    stored on PythonAnywhere in the git.Repo() as parameter.
                    Here the name of my directory is "test.pythonanywhere.com"
                    '''
            logger.debug("#CICD path : {}".format(BASE_DIR))
            repo = git.Repo(BASE_DIR)
            origin = repo.remotes.origin

            logger.info("#CICD updating project")
            origin.pull()
            logger.info("#CICD project updated successfully")

            update_requirements()

            return HttpResponse("Updated code on PythonAnywhere")

        except ConnectionError as ex:
            logger.error("#CICD update connection error : {}".format(str(ex)))
            return HttpResponse("Connection error while for updating code on PythonAnyWhere")
        except PermissionError as ex:
            logger.error("#CICD update Permission error : {}".format(str(ex)))
            return HttpResponse("Permission error while updating code on PythonAnyWhere")
        except TimeoutError as ex:
            logger.error("#CICD update timed out : {}".format(str(ex)))
            return HttpResponse("Timed out while updating code on PythonAnyWhere")
        except RuntimeError as ex:
            logger.error("#CICD Runtime error : {}".format(str(ex)))
            return HttpResponse("RuntimeError while updating code on PythonAnyWhere")
        except Exception as ex:
            logger.error("#CICD global exception : {}".format(str(ex)))
            return HttpResponse("Exception occured while updating code on PythonAnyWhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")


def update_requirements():
    env = os.getenv('VIRTUAL_ENV')
    logger.info("#CICD updating {} requirements".format(env))
    os.system(f"source {env}/bin/activate && pip install -r {BASE_DIR}/requirements.txt")
    logger.info("#CICD requirements updated for {}".format(env))
