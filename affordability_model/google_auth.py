import json

import httplib2
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.middleware import csrf
from django.shortcuts import redirect
from googleapiclient.discovery import build
from oauth2client import crypt
from oauth2client.client import OAuth2WebServerFlow, FlowExchangeError


def get_oauth2_flow(request):
    protocol = 'https://' if request.is_secure() else 'http://'
    host = request.META['HTTP_HOST']
    redirect_uri = protocol + host + reverse(oauth2)
    return OAuth2WebServerFlow(
            client_id=settings.GOOGLE_CLIENT_ID,
            client_secret=settings.GOOGLE_CLIENT_SECRET,
            scope=settings.GOOGLE_SCOPES,
            redirect_uri=redirect_uri
    )


class GoogleAuthBackend(ModelBackend):
    @staticmethod
    def _authenticate(userinfo):
        if userinfo.get('hd', 'gmail.com') not in settings.GOOGLE_APPS_DOMAIN_NAME:
            raise crypt.AppIdentityError("Wrong hosted domain.")
        email = userinfo.get('email')
        user = User.objects.get(username=email)
        if user and user.is_active:
            user.first_name = userinfo['given_name']
            user.last_name = userinfo['family_name']
            user.email = userinfo['email']
            user.save()
            return user
        else:
            raise crypt.AppIdentityError("Your account is inactive, please contact admin")

    def authenticate(self, username=None, password=None, **kwargs):
        user = super(GoogleAuthBackend, self).authenticate(username, password, **kwargs)
        if not user:
            userinfo = kwargs.get('userinfo')
            if userinfo:
                try:
                    user = self._authenticate(userinfo)
                except crypt.AppIdentityError as e:
                    user = None
        return user


def login(request):
    context = {
        'GOOGLE_CLIENT_ID': settings.GOOGLE_CLIENT_ID
    }
    oauth2_flow = get_oauth2_flow(request)

    csrf_token = csrf.get_token(request)
    state = {
        'csrf': csrf_token,
        'next': request.GET.get('next')
    }
    auth_uri = oauth2_flow.step1_get_authorize_url(state=json.dumps(state))
    return redirect(auth_uri)


def oauth2(request):
    state = json.loads(request.GET['state'])
    code = request.GET['code']

    oauth2_flow = get_oauth2_flow(request)
    try:
        credentials = oauth2_flow.step2_exchange(code=code)

        http = httplib2.Http()
        http = credentials.authorize(http)
        service = build('oauth2', 'v2', http=http)

        userinfo = service.userinfo().get().execute()
        user = auth.authenticate(userinfo=userinfo)
        if user:
            auth.login(request, user)

            next_page = state.get('next')
            return redirect(next_page)
        else:
            raise PermissionDenied()
    except FlowExchangeError as e:
        raise PermissionDenied(e)
