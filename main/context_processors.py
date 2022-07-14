from django.core.handlers.wsgi import WSGIRequest
from django_project.settings import PUBLIC_CONTEXT

def main(request: WSGIRequest):
    return PUBLIC_CONTEXT