from django.db import models
from datetime import date, datetime
from .. login.models import User

class Wallconvo(models.Model):
    content = models.CharField(max_length=1000)
    creator = models.ForeignKey(User, related_name="wallconvos", on_delete=models.PROTECT)
    wall_owner = models.ForeignKey(User, related_name="friendmessages", null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="wallconvolikes")
    privacy = models.BooleanField(default=False)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wallcomment(models.Model):
    content = models.CharField(max_length=1000)
    creator = models.ForeignKey(User, related_name="wallcomments", on_delete=models.PROTECT)
    wallconvo_owner = models.ForeignKey(Wallconvo, related_name="wallcomments", null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="wallcommentlikes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wallreply(models.Model):
    content = models.CharField(max_length=500)
    creator = models.ForeignKey(User, related_name="wallreplies", on_delete=models.PROTECT)
    hubcomment_owner = models.ForeignKey(Wallcomment, related_name="wallreplies", null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="wallreplylikes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
