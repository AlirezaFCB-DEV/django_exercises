import time
from django.http import StreamingHttpResponse
import asyncio
from asgiref.sync import sync_to_async


class Request_Timing_Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        #! This method just one call on startup.

    def __call__(self, req):
        response = self.get_response(req)

        if isinstance(response, StreamingHttpResponse):
            response["X-Streaming"] = "1"

        response["X-Processed"] = "1"
        return response

    def process_view(self, req, view_func, view_args, view_kwargs):
        # ? We Check If View Other Special Attrs
        if getattr(view_func, "require_login", False) and not req.user.is_authenticated:
            from django.http import JsonResponse
            return JsonResponse({"error": "auth required"}, status=401)
        #! none means continue processing (other middleware is also checked)
        return None

    def process_exception(self, req, exception):
        #! log
        import logging
        import traceback

        logging.exception("Unhandled exception in view")

        from django.http import JsonResponse

        return JsonResponse({"error": "internal server error"}, status=500)


class Async_Request_Logger_Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.is_async = asyncio.iscoroutinefunction(get_response)

    async def __call__(self, req):
        #!  Pre process (async-safe)
        start = asyncio.get_event_loop().time()

        if self.is_async:
            response = await self.get_response(req)
        else:
            response = await sync_to_async(self.get_response)(req)

        duration = asyncio.get_event_loop().time() - start

        response["X-Async-Duration-ms"] = str(int(duration * 1000))

        return response
