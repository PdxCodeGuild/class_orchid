from re import template
from urllib import request
from django.shortcuts import render, redirect
from .forms import ShoppingForm
from django.http import HttpResponse

from .models import GroceryItem
from django.views.decorators.http import require_POST
from django.template import loader
from django.db import models
from django.utils import timezone


def index(request):
    list = GroceryItem.objects.order_by("id")
    form = ShoppingForm()
    context = {"list":list, "form":form}
    return render(request, "grocerylist/index.html", context)

@require_POST
def additem(request):
    form = ShoppingForm(request.POST)
    if form. is_valid():
        new_item = GroceryItem(text= request.POST["text"]) 
       
        new_item.save()
    return (redirect("index"))

def completeitem(request, item_id):
    item = GroceryItem.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return (redirect("index"))

def deleteitem(request, item_id):
    item = GroceryItem.objects.get(pk=item_id)
    item.delete()
    return redirect("index")

def deleteall(request):
    GroceryItem.objects.all().delete()
    return redirect("index")

def undoitem(request, item_id):
    item = GroceryItem.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return (redirect("index"))


