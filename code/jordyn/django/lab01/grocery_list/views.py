from unicodedata import name
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.utils import timezone

from .models import GroceryList

# Create your views here.


def index(request):
    grocery_items = GroceryList.objects.all()
    context = {
        'items':grocery_items
    }
    return render(request, 'index.html', context) #needs work

def about(request):
    return HttpResponse("Fake About Stuff")

def complete(request, item_id):

    i = get_object_or_404(GroceryList, id=item_id) #uses django error conditional

    if i.is_complete == False:
        i.is_complete = True
    else:
        i.is_complete = False

    i.comp_date = timezone.now()
    i.save()

    return redirect('/grocery_list/')

    # i = GroceryList.objects.get(id=item_id) #needs error conditional

def delete(request, item_id):
    i = get_object_or_404(GroceryList, id=item_id)
    i.delete()

    return redirect('/grocery_list/')

def add(request):

    if request.method == 'POST':
        item_name = request.POST['add_item']
        if item_name != '':
            GroceryList.objects.create(name=item_name)
        else:
            print('empty space')

    return redirect('/grocery_list/')

def description(request, item_id):
    i = get_object_or_404(GroceryList, id=item_id)
    
    if request.method == 'POST':
        i.description = request.POST['add_desc']
        i.save()

    return redirect('/grocery_list/')
