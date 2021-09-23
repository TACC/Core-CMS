import inspect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib import auth as auth
from django.utils.module_loading import import_string
from django.contrib.auth.backends import RemoteUserBackend
import requests
import logging
from django.conf import settings

UserModel = get_user_model()

logger = logging.getLogger(__name__)

def load_backend(path):
    return import_string(path)()

def verify_and_auth(request):
    user = auth.authenticate(request)
    if user:
        # User is valid.  Set request.user and persist user in the session by logging the user in.
        request.user = user
        auth.login(request, user)
        response = HttpResponseRedirect(request.GET.get('next', \
                                                        getattr(settings, 'LOGIN_REDIRECT_URL', '/workbench/dashboard/')))
    else:
        response = HttpResponseRedirect('/')
    return response


class CorePortalAuthBackend(ModelBackend):
    """
        Validates core portal session
        Extends Django ModelBackend, parts of this were taken from Django's source:
        https://github.com/django/django/blob/stable/2.2.x/django/contrib/auth/backends.py#L128
    """
    create_unknown_user = True

    def authenticate(self, request):
        response = requests.get('{0}/api/users/auth/'.format( \
            getattr(settings, 'CEP_AUTH_VERIFICATION_ENDPOINT', 'http://django:6000')),
            cookies={'coresessionid': request.COOKIES.get('coresessionid')})
        user_data = response.json()
        if user_data is None or user_data['username'] is None:
            return None
        username = user_data['username']
        email = user_data['email']
        first_name = user_data['first_name']
        last_name = user_data['last_name']

        if request.user.is_authenticated:
            self._remove_invalid_user(request)

        if self.create_unknown_user:
            user, created = UserModel._default_manager.get_or_create(**{
                UserModel.USERNAME_FIELD: username
            })
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            if created:
                args = (request, user)
                try:
                    inspect.getcallargs(self.configure_user, request, user)
                except TypeError:
                    args = (user,)
                    warnings.warn(
                        'Update %s.configure_user() to accept `request` as '
                        'the first argument.'
                        % self.__class__.__name__, RemovedInDjango31Warning
                    )
                user = self.configure_user(*args)
        else:
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
            except UserModel.DoesNotExist:
                pass
        return user if self.user_can_authenticate(user) else None

    def _remove_invalid_user(self, request):
        """
        Remove the current authenticated user
        """
        try:
            stored_backend = load_backend(request.session.get(auth.BACKEND_SESSION_KEY, ''))
        except ImportError:
            # backend failed to load
            auth.logout(request)
        else:
            if isinstance(stored_backend, RemoteUserBackend):
                auth.logout(request)

    def configure_user(self, request, user):
        """
        Configure a user after creation and return the updated user.
        By default, return the user unmodified.
        """
        return user
