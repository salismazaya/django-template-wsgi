from django.http import HttpRequest
from django.conf import settings
from django.utils.crypto import get_random_string
from django.templatetags.static import static

def main(request: HttpRequest):
    return settings.PUBLIC_CONTEXT

def debug(request: HttpRequest):
    return {
        'tailwind_css_static': "{}?v={}".format(static('css/tailwind.css'), get_random_string())
    }

def production(request: HttpRequest):
    return {
        'tailwind_css_static': static('css/tailwind.min.css')
    }