from django.shortcuts import render, redirect, HttpResponse
from datetime import date, datetime
from django.contrib import messages
from .. login.models import User
from . models import Wallconvo, Wallcomment, Wallreply
#dashboard views

def index(request, username):
        if request.method == 'GET':
            profile = User.objects.get(username=username)
            allfriends = profile.friend.all()
            context = {
                "owner": User.objects.get(username=username),
                "user": User.objects.get(username=request.session['username']),
                "all_friends":  allfriends,
                "all_convos": Wallconvo.objects.filter(wall_owner=User.objects.get(username=username)).order_by('-created_at')
            }
            return render(request, 'dashboard/index.html', context)
        return redirect('/')

def postconvo(request, username):
    if request.method == 'POST':
        newconvo = Wallconvo.objects.create(content=request.POST['newconvo'], creator=User.objects.get(username=request.session['username']), wall_owner=User.objects.get(username=username))
        if 'privacy' in request.POST:
            newconvo.privacy = True
            newconvo.save()
            print("true")
        print("added new convo")
    return redirect('/dashboard/' + str(username))

def postreply(request, username, id):
    return HttpResponse("post a reply")

def editprofile(request, username):
        if request.method == 'GET':
            if request.session['username'] == username:
                context = {
                    "user": User.objects.get(username=request.session['username'])
                }
                return render(request, 'dashboard/editprofile.html', context)                
            return redirect('/dashboard/' + request.session['username'])
        return redirect('/')

def updateprofile(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        bio = str(request.POST['bio'])
        if len(bio) > 0 and len(bio) > 1000:
            return HttpResponse("bio too long")
        elif len(bio) > 0:
            user.bio = bio
            user.save()
            return redirect('/dashboard/' + request.session['username'])

def allfriends(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=request.session['username'])
        owner = User.objects.get(username=username)
        all_friends = owner.friend.all()
        context = {
            "user": user,
            "friends": all_friends,
            "owner": owner
        }
    return render(request, 'dashboard/allfriends.html', context)

def addfriend(request, username):
    if request.method =='POST':
        friend_adding = User.objects.get(username=request.session['username'])
        friend_being_added = User.objects.get(username=username)
        friend_adding.friend.add(friend_being_added)
        friend_adding.save()
        print("added friend")
        return redirect('/dashboard/' + username)
    return redirect('/dashboard/' + request.session['username'])

def removefriend(request, username):
    if request.method =='POST':
        friend_removing = User.objects.get(username=request.session['username'])
        friend_being_removed = User.objects.get(username=username)
        friend_removing.friend.remove(friend_being_removed)
        friend_removing.save()
        print("removed friend")
        return redirect('/dashboard/' + username)
    return redirect('/dashboard/' + request.session['username'])

def admin(request, username):
    if request.session['username'] != "Unruly_SpaceCat":
        return redirect('/logout')
    else:
        all_cats = User.objects.exclude(id=1)
        context = {
                "cats": all_cats
            }
        return render(request, 'dashboard/admin.html', context)

def adminmake(request, username):
    if request.session['username'] != "Unruly_SpaceCat":
        return redirect('/logout')
    else:
        new_mod = User.objects.get(username=request.POST['catmod'])
        new_mod.user_level = "admin"
        new_mod.save()
        print("added new moderator")
        return redirect('/dashboard/' + request.session['username'] + '/admin')

def adminremove(request, username):
    if request.session['username'] != "Unruly_SpaceCat":
        return redirect('/logout')
    else:
        new_mod = User.objects.get(username=request.POST['un-mod'])
        new_mod.user_level = "generic"
        new_mod.save()
        print("removed moderator")
        return redirect('/dashboard/' + request.session['username'] + '/admin')

def adminban(request, username):
    if request.session['username'] != "Unruly_SpaceCat":
        return redirect('/logout')
    else:
        banned_user = User.objects.get(username=request.POST['catban'])
        banned_user.delete()
        print("Banned User")
        return redirect('/dashboard/' + request.session['username'] + '/admin')

def private(request, username):
    if request.session['username'] == username:
        user = User.objects.get(username=username)
        if user.privacy == True:
            user.privacy = False
            user.save()
        else:
            user.privacy = True
            user.save()
        return redirect('/dashboard/' + str(username))
    return redirect('/dashboard/' + request.session['username'])