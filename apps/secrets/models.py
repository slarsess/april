# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..logapp.models import User
from django.db import models

# Create your models here.
class SecretManager(models.Manager):
    def validate_secret(self, data):
        errors = []
        # user = User.objects.get(id=data['id'])
        if len(data['secret']) < 1:
            errors.append("Your secret cannot be blank")
        if len(data['secret']) > 255:
            errors.append("Brevity is the soul of wit")
        if errors:
            return (False, errors)
        else:
            new_secret = Secret.objects.create(
                secret = data['secret'],
            )
            return (True, new_secret)
    def DeleteSecret(self, data):
        try:
            objDelete = Secret.objects.get(id=data)
            if objDelete.created_by == request.session['id']:
                objDelete.delete()
            return True
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            return e.message


class Secret(models.Model):
    secret = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    # user_id = models.ForeignKey('logapp.User')
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creators")#cascades a deleted user to delete this field
    objects = SecretManager()


# liked_by = models.ManytoManyField(User, related_name = "fans")
