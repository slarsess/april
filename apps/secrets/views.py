# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import F
from django.shortcuts import render, redirect, HttpResponse, reverse
from ..logapp.models import User
from models import Secret
from django.contrib import messages

# Create your views here.
#https://docs.djangoproject.com/en/1.7/ref/models/queries/ <--import F ??

def recent(request): #this is actually an index page for this app
    if 'id' not in request.session:
        messages.error(request, "You must be logged in first, ie why is the id not in session?")
        return redirect('logapp:index')
    context = {
    "posts": Secret.objects.order_by("-created_at")[:5]
    }
    return render(request, "secrets/recent.html", context)

def popular(request):
    if 'id' not in request.session:
        messages.error(request, "You must be logged in first")
        return redirect('logapp:index')
    context = {
    "posts": Secret.objects.order_by("-likes")[:10]
    }
    return render (request, 'secrets/popular.html', context)

def post(request):
    if request.method =="POST":
        valid, data = Secret.objects.validate_secret(request.POST)
        if valid == True:
            print "successful post"
        else:
            for error in data:
                messages.error(request, error)
            return redirect ('secrets:recent')#probably not needed, but kept incase I want to send the user elsewhere
    return redirect('secrets:recent')

def like(request, id):
    secret_like = Secret.objects.get(id=id)
    secret_like.likes = F('likes') + 1
    secret_like.save()
    return redirect('secrets:recent')

def destroy(request, secret_id):#not working yet
    retVal = Secret.objects.DeleteSecret(request.session['id'],secret_id)
    if retVal:
        return redirect('secrets:home')
    else:
        messages.error(request, retVal)
        return redirect ('secrets:recent')
