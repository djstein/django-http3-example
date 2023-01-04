class LowercaseHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response.headers = {
            key.lower(): value for key, value in response.headers.items()
        }
        return response
