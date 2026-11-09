from django.shortcuts import render
from .models import YoutubeUser
from django.core.cache import cache
# Create your views here.

def users_list(request):
    users = cache.get('users_data')

    if not users:
        print("Cache miss: Fetching data from database")
        users = YoutubeUser.objects.all()
        cache.set('users_data', 'users', timeout=60)  #60 seconds
    else:
        print("Cache hit: Fetching data from cache")
    return render(request,'users_list.html',{"users":users})