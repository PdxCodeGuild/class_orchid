

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpRequest, Http404
from .models import GroceryItem
from django.template import loader

def index(request):
    grocery_items = GroceryItem.objects.order_by('created_date')
    # output = ', '.join([a.text_description for a in grocery_items])
    context = {
        'grocery_items':grocery_items,
    }
    return render(request, 'grocery_list_app/index.html', context)

def add(request):
    if request.method == 'POST':
        new_item = request.POST.get('grocery')
        GroceryItem.objects.create(text_description=new_item)
    return redirect('/')

def completed(request, grocery_items_id):
    grocery_item = GroceryItem.objects.get(id = grocery_items_id)
    grocery_item.completed = True
    grocery_item.save()
    return redirect('/')

def delete(request, grocery_items_id):
    delete = GroceryItem.objects.get(id=grocery_items_id)
    delete.delete()
    return redirect('/')

def undo(request, grocery_items_id):
    grocery_item = GroceryItem.objects.get(id = grocery_items_id)
    grocery_item.completed = False
    grocery_item.save()
    return redirect('/')