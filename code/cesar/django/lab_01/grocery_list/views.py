from cgitb import html
from importlib.resources import contents
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, redirect
from django.utils import timezone


from .models import GroceryItem


def index(request: HttpRequest):
    if request.method == 'POST':
        description = request.POST.get('description')

        GroceryItem.objects.create(
            description=description

        )
        return redirect('/list')
    grocery_list = GroceryItem.objects.all()
    context = {
        'grocery_list': grocery_list
    }

    return render(request, 'index.html', context)


def detail(request, item_id):
    try:
        item = GroceryItem.objects.get(pk=item_id)
    except GroceryItem.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'detail.html', {'item': item})


def completed(request, item_id):

    completed_item = GroceryItem.objects.get(pk=item_id)
    completed_item.completed = True
    completed_item.save()
    return redirect('/list/')


def item_undo(request, item_id):
    item_undo = GroceryItem.objects.get(pk=item_id)
    item_undo.completed = False
    item_undo.save()
    return redirect('/list/')


def delete_item(request, item_id):
    item_delete = GroceryItem.objects.get(pk=item_id)
    item_delete.delete()
    return redirect('/list')
