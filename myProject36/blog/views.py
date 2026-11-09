from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache

# Create your views here.
def users_list(request):
    users = cache.get('users_list')

    if not users:
        print("Cache miss: Querying database for users.")
        users = UserProfile.objects.all()
        cache.set('users_list', users, timeout=100)
    else:
        print('Cache hot: retrieved users from cache')
    return render(request, 'users_list.html', {"users":users})