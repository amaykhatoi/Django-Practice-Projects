from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_cookie(request):
    response = HttpResponse('Cookie Set Successfully')
    response.set_cookie('username','Mohit Kumar',max_age=60*60*24*7)
    response.set_cookie('course','Django Full Course',max_age=60*60*24*7)
    return response

def get_cookie(request):
    username = request.COOKIES.get('username','Guest')
    course = request.COOKIES.get('course','No course selected')
    # return HttpResponse(f'UserName:{username} , Course: {course}')
    if 'username' in request.COOKIES:
        return HttpResponse(f"UserName:{username} , Course: {course}")
    else:
        return HttpResponse("No cookie found")

def delete_cookie(request):
    response = HttpResponse("Cookie Delete Successfully.")
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response