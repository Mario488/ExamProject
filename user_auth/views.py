from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_method
from django.contrib.auth import login as login_method
from django.contrib import messages
from event import models
from django.contrib.auth.models import User

def profile(request):
    username = request.user.username
    bookedEvent = models.BookedEvent.objects.filter(User=username)
    if request.method == "POST":
        del_res = request.POST['deleteReservation']
        event_del = models.BookedEvent.objects.filter(Name=del_res)
        event_del.delete()
        return render(request, 'profile.html', {'username': username, 'events': bookedEvent})
    return render(request, 'profile.html', {'username': username, 'events': bookedEvent})

def logout(request):
    logout_method(request)
    messages.success(request, 'You\'ve been logged out')
    return redirect('home')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_method(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('home')
        else:
            return render(request, 'login.html', {'message': 'Invalid username or password!'})
    return render(request, 'login.html', {'message': ''})

from django.contrib.auth.models import User

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken.')
                return render(request, 'sign_up.html', {'form': form})
            else:
                form.save()
                messages.success(request, "Account, Successfully Created!")
                return redirect('login')
        else:
            messages.error(request, "Password restrictions must match! Try again.")
            form = RegisterForm()
            return render(request, 'sign_up.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'sign_up.html', {'form': form})





