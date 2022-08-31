
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from .models import GroceryItem
from django.template import loader

def index(request):
    grocery_items = GroceryItem.objects.order_by('created_date')
    # output = ', '.join([a.text_description for a in grocery_items])
    context = {
        'grocery_items':grocery_items,
    }
    return render(request, 'grocery_list_app/index.html', context)

def grocery_list(request, grocery_items_id):
    try:
        grocery_items = GroceryItem.objects.get(pk = grocery_items_id)
    except GroceryItem.DoesNotExist:
        raise Http404("Not an item")
    return render(request, 'grocery_list_app/detail.html', {grocery_items:"grocery_items"})

def completed(request, grocery_items_id):
    response = "You're looking at the completed item %s."
    return HttpResponse(response % grocery_items_id)