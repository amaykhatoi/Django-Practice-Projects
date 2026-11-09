from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_session(request):
    request.session['username'] = 'Amay'
    request.session['course'] = 'Django Full Course'
    return HttpResponse("Session data saved Successfully.")

def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'Not enrolled')
    return HttpResponse(f"Welcome : {username}, You are learning {course}")

def delete_session(request):
    request.session.flush()
    return HttpResponse("All session data deleted successfully.")
    