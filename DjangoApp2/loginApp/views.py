from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    if(request.user.is_anonymous):
        return redirect('/loginUser')
    return render(request, 'index.html')

def loginUser(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        pw = request.POST.get('pw')
        print('Check entered details:', username, pw)
        user = authenticate(username=username, password=pw)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/store')
        else:
            # No backend authenticated the credentials
            # add message saying that cred is invalid
            messages.warning(request, "Invalid credentials!")
            # messages.warning(request, "Your account expires in three days.")
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/loginUser')