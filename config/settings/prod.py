from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
        env('IP_ADDRESS'), 'example.com', 'www.example.com', 'localhost'
    ]
