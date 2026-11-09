from django.contrib import admin
from .models import YoutubeUser
from django.core.cache import cache
from django.contrib import messages
# Register your models here.

@admin.action(description='Clear Users Cache')
def clear_users_cache(modeladmin, request, queryset):
    cache.delete('users_data')
    messages.success(request,"users cache cleared successfully")

@admin.register(YoutubeUser)
class YoutubeUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribers')
    actions = [clear_users_cache]
