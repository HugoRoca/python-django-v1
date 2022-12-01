from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'message': 'From view'
    })


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Welcome {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Incorrect username or password.')

    return render(request, 'login.html', {

    })