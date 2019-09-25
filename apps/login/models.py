from __future__ import unicode_literals
from django.db import models
import re
from datetime import date, datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['uname']) > 25:
            errors['uname'] = "Username cannot be more than 25 characters"
        unavailable = User.objects.filter(username=postData['uname'])
        if len(unavailable) > 0:
            errors['unameinvalid'] = "Username is already taken"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["emailinvalid"] = "Email is not in correct format"
        if len(postData['pw1']) < 8:
            errors['passwordlength'] = "Password must be at least 8 characters"
        if postData['pw1'] != postData['pw2']:
            errors['passwordinvalid'] = "Passwords don't match"
        return errors

class User(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=65)
    user_level = models.CharField(max_length=10, default="generic")
    avatar = models.IntegerField(default="13")
    bio = models.CharField(max_length=1000, default="")
    friend = models.ManyToManyField('self', related_name="friends")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    privacy = models.BooleanField(default=False)
    objects = UserManager()