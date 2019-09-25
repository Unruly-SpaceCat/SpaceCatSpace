from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .. login.models import User
from . models import Hubconvo, Hubcomment, Hubreply
from datetime import date, datetime, timedelta
#kithub views

def index(request):
    if request.method == 'GET':
        if 'username' in request.session:
            context = {
                "all_convos":  Hubconvo.objects.all().order_by('-created_at'),
                "user": User.objects.get(username=request.session['username'])
            }
            return render(request, 'kithub/index.html', context)
        return HttpResponse("User not authorized")

def show(request, id):
    if request.method == 'GET':
        convo = Hubconvo.objects.get(id=id)
        allcomments = convo.hubcomments.all().order_by('-created_at')
        context = {
            "convo": convo,
            "all_comments":  allcomments,
            "user": User.objects.get(username=request.session['username'])
        }
        return render(request, 'kithub/convos.html', context)
    return HttpResponse("Method not permitted")

def addconvo(request):
    if request.method == 'POST':
        creator = User.objects.get(username=request.session['username'])
        creator.hubconvos.create(content=request.POST['newconvo'])
        print("newconvo added")
        return redirect('/kithub')
    return redirect('/kithub')

def likeconvo(request, id):
    if request.method == 'GET':
        user = User.objects.get(username=request.session['username'])
        convo = Hubconvo.objects.get(id=id)
        user.hubconvolikes.add(convo)
        return redirect('/kithub')
    return redirect('/kithub')

def deletecomment(request, id1, id2):
    if request.method == 'GET':
        if 'username' in request.session:
            user = User.objects.get(username=request.session['username'])
            comment_to_delete = Hubcomment.objects.get(id=id2)
            commentowner = comment_to_delete.creator
            if user.username == commentowner.username or user.user_level != 'generic':
                comment_to_delete.delete()
                print("comment deleted")
                return redirect('/kithub/' + str(id1))
            return HttpResponse("User not authorized for this action")
        return HttpResponse("Action not authorized")
    return redirect ('/kithub')

def addcomment(request, id):
    if request.method == 'POST':
        Hubcomment.objects.create(content=request.POST['convocomment'], creator=User.objects.get(username=request.session['username']), hubconvo_owner=Hubconvo.objects.get(id=id))
        print("new comment added")
        return redirect('/kithub/' + str(id))
    return redirect('/kithub')

def likecomment(request, id1, id2):
    if request.method == 'GET':
        if 'username' in request.session:
            user = User.objects.get(username=request.session['username'])
            comment = Hubcomment.objects.get(id=id2)
            user.hubcommentlikes.add(comment)
            return redirect('/kithub/' + str(id1))
        return redirect('/kithub')
    return redirect('/kithub')

def addreply(request, id1, id2):
    if request.method == 'POST':
        Hubreply.objects.create(content=request.POST['commentreply'], creator=User.objects.get(username=request.session['username']), hubcomment_owner=Hubcomment.objects.get(id=id2))
        print("new comment added")
        return redirect('/kithub/' + str(id1))
    return redirect('/kithub')

def deleteconvo(request, id):
    if request.method == 'GET':
        convo = Hubconvo.objects.get(id=id)
        user = User.objects.get(username=request.session['username'])
        if user == convo.creator or user.user_level != 'generic':
            convo.delete()
            print("deleted convo")
            return redirect('/kithub')
        else:
            return HttpResponse("User not authorized")
    return redirect('/kithub')

def apod(request):
    if request.method == 'GET':
        context = {
            "user": User.objects.get(username=request.session['username'])
        }
    return render(request, 'kithub/apod.html', context)