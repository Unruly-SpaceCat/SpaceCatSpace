from django.shortcuts import render, redirect, HttpResponse
import bcrypt
import re
from django.contrib import messages
from .models import User
#login views

def index(request):
    if request.method == 'GET':
        return render(request, 'login/index.html')
    return redirect('/')

def adduser(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pword = bcrypt.hashpw(request.POST['pw1'].encode(), bcrypt.gensalt())
            new_cat = User.objects.create(username=request.POST['uname'], email=request.POST['email'], password=pword)
            request.session['username'] = request.POST['uname']
            print(request.session['username'])
            print("added" + new_cat.username)
            return redirect("/dashboard/" + request.session['username'])
    return redirect('/')

def login(request):
    if request.method == 'POST':
        user_to_auth = User.objects.filter(username=request.POST['username'])
        errors = {}
        if len(user_to_auth) == 0:
            errors['username'] = "Username does not exist"
            return redirect('/')
        user_to_auth = User.objects.get(username=request.POST['username'])
        if not bcrypt.checkpw(request.POST['pwrd'].encode(), user_to_auth.password.encode()):
            errors['password'] = "Password does not match this user."
            return redirect('/')
        else:
            request.session['username'] = request.POST['username']
            return redirect('/dashboard/'+request.session['username'])
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
    