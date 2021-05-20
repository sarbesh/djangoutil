from datetime import timedelta, datetime
from django.conf import settings
from django.utils.timezone import make_aware

import pytz
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class BearerAuthentication(TokenAuthentication):
    """
        Simple token based authentication.
        Clients should authenticate by passing the token key in the "Authorization"
        HTTP header, prepended with the string "Bearer ".  For example:
        Authorization: Bearer 401f7ac837da42b97f613d789819ff93537bee6a
    """
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        # This is required for the time comparison
        now = datetime.now()
        now = now.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))

        if token.created < make_aware(now.now() - timedelta(days=60)):
            raise exceptions.AuthenticationFailed('Token has expired')

        return token.user, token

