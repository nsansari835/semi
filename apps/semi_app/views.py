from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from models import *
from django.contrib import messages

def index(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, "semi_app/index.html", context)
def new(request):
    return render(request, "semi_app/new.html")
def create(request):
    errors = User.objects.validator(request.POST, "create")
    if len(errors): 
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/semi_app/new") 
    else:
        newuser = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
        return redirect("/semi_app/"+str(newuser.id))
def show(request, id):
    print id
    context = {
        "user" : User.objects.get(id=int(id))
    }
    return render(request, "semi_app/show.html", context) 
def edit(request, id):
    context = {
        "user" : User.objects.get(id=int(id))
    }
    return render(request, "semi_app/edit.html", context)
def update(request, id):
    errors = User.objects.validator(request.POST, "update")
    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/semi_app/new")
    else:
        User.objects.filter(id=int(id)).update(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
        return redirect("/semi_app/"+id)
def destroy(request, id):
    User.objects.get(id=int(id)).delete()
    return redirect('/semi_app')