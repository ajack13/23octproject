import os

from django.core.exceptions import ImproperlyConfigured


def read_env(env_name):
    try:
        return os.environ[env_name]
    except KeyError:
        raise ImproperlyConfigured(f"Environment Variable : {env_name} Missing !")
