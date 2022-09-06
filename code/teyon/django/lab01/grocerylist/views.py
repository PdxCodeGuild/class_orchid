from django.urls import reverse
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import GroceryItem

def index(request):
    grocery_list = GroceryItem.objects.all()
    complete = grocery_list.filter(completed=True)
    incomplete = grocery_list.filter(completed=False)
    context = {
        'complete': complete,
        'incomplete': incomplete,
    }

    return render(request, 'grocerylist/index.html', context)

def create(request):
    GroceryItem(text_description= request.POST['add-item']).save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk= grocery_item_id)
    if grocery_item.completed == False:
        grocery_item.completed = True
    else:
        grocery_item.completed = False
    
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def incomplete(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk= grocery_item_id)
    if grocery_item_id.completed == True:
        grocery_item_id.completed = False
    else:
        grocery_item_id.completed = True
    
    grocery_item.save

    return HttpResponseRedirect(reverse('grocery_list:index'))


def delete(request, grocery_item_id):
    grocery_item = get_object_or_404('grocery_list', pk= grocery_item_id)
    grocery_item.delete

    return HttpResponseRedirect(reverse('grocery_list', pk= grocery_item_id))
