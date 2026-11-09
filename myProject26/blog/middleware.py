import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class SimpleLogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(f"[{datetime.datetime.now()}] Request url: {request.path}")

    def process_response(self, request,response):
        print(f"[{datetime.datetime.now()}] Responce Status code : {response.status_code}")
        return response

