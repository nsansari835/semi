from __future__ import unicode_literals
from django.db import models
import re
LETTER_REGEX = re.compile(r"^[a-zA-Z]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

class BlogManager(models.Manager):
    def validator(self, postData, valid):
        errors = {}
        if len(postData[ "first_name" ]) < 1:
            errors["first_name"] = "First name cannot be blank"
        elif not LETTER_REGEX.match(postData[ "first_name" ]):
            errors["first_name"] = "FIrst name must be letters only"
        if len(postData[ "last_name" ]) < 1:
            errors["last_name"] = "last name cannot be blank"
        elif not LETTER_REGEX.match(postData[ "last_name" ]):
            errors["last_name"] = "Last name must be letters only"
        if len(postData[ "email" ]) < 1:
            errors["email"] = "Email cannot be blank"
        elif not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Must be valid email"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()