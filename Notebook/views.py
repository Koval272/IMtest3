# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Notebook
from django.shortcuts import render

def index(request):
    tech = Notebook.objects.all()
    return render(request, "main.html", {'tech': tech})

def check(request):
    return render(request, "view.html")

def add(request):
    return render(request, "add.html")


def create(request):
    any = Notebook()
    any.audience = request.POST.get("au")
    any.brand = request.POST.get("brand")
    any.model = request.POST.get("model")
    any.tp = request.POST.get("type")
    any.cpu = request.POST.get("cpu")
    any.gpu = request.POST.get("gpu")
    any.ram = request.POST.get("ram")
    any.state = request.POST.get("state")
    any.date = request.POST.get("dateBuy")
    any.use = request.POST.get("dateUse")
    any.person = request.POST.get("person")
    any.term = request.POST.get("term")
    any.save()
    return HttpResponseRedirect("/")

def edit(request, id):
    try:
        any = Notebook.objects.get(id=id)
        if request.method == "POST":
            any.audience = request.POST.get("au")
            any.ram = request.POST.get("ram")
            any.state = request.POST.get("state")
            any.person = request.POST.get("person")
            any.term = request.POST.get("term")
            any.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {'tech': any})
    except Notebook.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")