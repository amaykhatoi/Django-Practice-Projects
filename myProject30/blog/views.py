from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.http import HttpResponse
# Create your views here.

def send_bulk_email(request):
    message1 = ('Welcome User 1','Hello User 1 welcome to our platfrom','amaykahtoi@gmail.com',['amaykhatoi07@gmail.com'])
    message2 = ('Welcome User 2','Hello User 2 welcome to our platfrom','amaykahtoi@gmail.com',['amaykhatoi07@gmail.com'])
    message3 = ('Welcome User 3','Hello User 3 welcome to our platfrom','amaykahtoi@gmail.com',['amaykhatoi07@gmail.com'])

    send_mass_mail((message1, message2, message3), fail_silently=False)
    return HttpResponse('Bulk emials send successfully.')