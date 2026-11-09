from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def show_msg(request):
    messages.debug(request,'This is Debug Message')
    messages.info(request,'This is Info Message')
    messages.success(request,'This is Info success')
    messages.warning(request,'This is Info warning')
    messages.error(request,'This is Info error')

    return render(request, 'message.html')