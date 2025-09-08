import time


class Request_Timing_Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        #! This method just one call on startup.

    def __call__(self, req):
        #! This method for all req callable.

        start = time.time()  # ? Start Time
        # ? Resume Process To Rest Of Middlewares And In End View
        response = self.get_response(req)
        duration = time.time() - start  # ? Run Time

        # ? Add header for watching response time
        response["X-Request-Duration-ms"] = str(int(duration * 1000))
        return response
