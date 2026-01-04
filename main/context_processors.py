from django.conf import settings
from django.http import HttpRequest
from django.templatetags.static import static
from django.utils.crypto import get_random_string


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