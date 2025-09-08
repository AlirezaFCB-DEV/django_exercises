import time


class Request_Timing_Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        #! This method just one call on startup.

    def __call__(self, req):
        #! This method for all req callable.

        if not self.enabled:
            return self.get_response(req)

        start = time.time()  # ? Start Time
        # ? Resume Process To Rest Of Middlewares And In End View
        response = self.get_response(req)
        duration = time.time() - start  # ? Run Time

        # ? Add header for watching response time
        response["X-Request-Duration-ms"] = str(int(duration * 1000))
        return response

    def process_view(self, req, view_func, view_args, view_kwargs):
        # ? We Check If View Other Special Attrs
        if getattr(view_func, "require_login", False) and not req.user.is_authenticated:
            from django.http import JsonResponse
            return JsonResponse({"error": "auth required"}, status=401)
        #! none means continue processing (other middleware is also checked)
        return None
