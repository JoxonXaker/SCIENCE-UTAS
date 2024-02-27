from django.conf import settings
from django.utils.translation import get_language


class LanguageMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/admin'):
            response.set_cookie(key=settings.LANGUAGE_COOKIE_NAME, value=settings.LANGUAGE_CODE, max_age=100000000)
        else:
            response.set_cookie(key=settings.LANGUAGE_COOKIE_NAME, value=get_language(), max_age=100000000)
        return response
