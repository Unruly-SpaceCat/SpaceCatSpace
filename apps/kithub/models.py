from django.db import models
from datetime import date, datetime
from .. login.models import User

class Hubconvo(models.Model):
    content = models.CharField(max_length=500)
    creator = models.ForeignKey(User, related_name="hubconvos", on_delete=models.PROTECT)
    likes = models.ManyToManyField(User, related_name="hubconvolikes")   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Hubcomment(models.Model):
    content = models.CharField(max_length=500)
    creator = models.ForeignKey(User, related_name="hubcomments", on_delete=models.PROTECT)
    hubconvo_owner = models.ForeignKey(Hubconvo, related_name="hubcomments", null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="hubcommentlikes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Hubreply(models.Model):
    content = models.CharField(max_length=500)
    creator = models.ForeignKey(User, related_name="hubreplies", on_delete=models.PROTECT)
    hubcomment_owner = models.ForeignKey(Hubcomment, related_name="hubreplies", null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="hubreplylikes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


