from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def user_login(request):
    return render(request, 'authentication/login.html')


# Check if user typed the rigth credentials
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )


# Show that the user has logged in
def show_user(request):
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })
