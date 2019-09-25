from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .. login.models import User
#avatars views

def index(request):
    if request.method == 'GET':
        context = {
            "user":  User.objects.get(username=request.session['username'])
        }
        userlevel=User.objects.get(username=request.session['username'])
        print(userlevel.user_level)
        return render(request, 'avatars/index.html', context)
    return redirect('/')

def update(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.session['username'])
        user.avatar = request.POST['avatar']
        user.save()        
        return redirect('/avatars')
    return HttpResponse('not allowed')


# Create your views here.
