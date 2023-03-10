class SetAuthHeaderFromCookie:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            auth_token = request.COOKIES.get('access_token')
            if auth_token:
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {auth_token}'

        response = self.get_response(request)
        return response
