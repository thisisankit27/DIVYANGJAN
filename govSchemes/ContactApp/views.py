from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def contactSend(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name)
        if email is None:
            messages.info(request, 'No Email Provided')
            return redirect('/')
