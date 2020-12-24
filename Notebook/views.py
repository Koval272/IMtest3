# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Notebook, Repairs
from .forms import NotebookFilterForm
from django.shortcuts import render


def index(request):
    tech = Notebook.objects.all()
    form = NotebookFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["num_audience"]:
            tech = tech.filter(audience=form.cleaned_data["num_audience"])
        if form.cleaned_data["num_brand"]:
            tech = tech.filter(brand=form.cleaned_data["num_brand"])
        if form.cleaned_data["num_model"]:
            tech = tech.filter(model=form.cleaned_data["num_model"])
        if form.cleaned_data["num_type"]:
            tech = tech.filter(tp=form.cleaned_data["num_type"])
        if form.cleaned_data["num_gpu"]:
            tech = tech.filter(gpu=form.cleaned_data["num_gpu"])
        if form.cleaned_data["num_ram"]:
            tech = tech.filter(ram=form.cleaned_data["num_ram"])
        if form.cleaned_data["num_state"]:
            tech = tech.filter(state=form.cleaned_data["num_state"])
        if form.cleaned_data["num_term"]:
            tech = tech.filter(term=form.cleaned_data["num_term"])
    return render(request, "main.html", {"tech": tech, "form":form})

def index1(request):
    tech = Repairs.objects.all()
    return render(request, "repairs.html", {'tech': tech})

def auF(request, audience):
    tech = Notebook.objects.all().filter(audience=audience)
    return render(request, "main.html", {'tech': tech})

def brandF(request, brand):
    tech = Notebook.objects.all()
    if brand == request.POST.get("brandF"):
        tech = Notebook.objects.all().filter(brand=request.POST.get("brandF"))
    if brand == request.POST.get("modelF"):
        tech = Notebook.objects.all().filter(model=request.POST.get("modelF"))
    if brand == request.POST.get("typeF"):
        tech = Notebook.objects.all().filter(tp=request.POST.get("typeF"))
    """any.cpu = request.POST.get("cpu")
    any.ram = request.POST.get("ram")
    any.state = request.POST.get("state")
    any.date = request.POST.get("dateBuy")
    any.use = request.POST.get("dateUse")
    any.person = request.POST.get("person")"""
    return render(request, "main.html", {'tech': tech})

def add(request):
    return render(request, "add.html")


def create(request):
    any = Notebook()
    any.audience = request.POST.get("au")
    any.brand = request.POST.get("brand")
    any.model = request.POST.get("model")
    any.tp = request.POST.get("type")
    any.cpu = request.POST.get("cpu")
    any.ram = request.POST.get("ram")
    any.state = request.POST.get("state")
    any.date = request.POST.get("dateBuy")
    any.use = request.POST.get("dateUse")
    any.person = request.POST.get("person")
    any.term = request.POST.get("term")
    any.save()
    if any.state == "В ремонте":
        new = Repairs()
        new.rBrand = any.brand
        new.rModel = any.model
        new.cause = request.POST.get("cause")
        new.rDate = request.POST.get("rDate")
        new.save()
    return HttpResponseRedirect("/")

def edit(request, id):
    try:
        any = Notebook.objects.get(id=id)
        if request.method == "POST":
            any.audience = request.POST.get("au")
            any.state = request.POST.get("state")
            any.person = request.POST.get("person")
            any.term = request.POST.get("term")
            any.save()
            if any.state != "Исправен":
                new = Repairs()
                new.rBrand = any.brand
                new.rModel = any.model
                new.cause = request.POST.get("cause")
                new.rDate = request.POST.get("rDate")
                new.save()
                return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {'tech': any})
    except Notebook.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
  