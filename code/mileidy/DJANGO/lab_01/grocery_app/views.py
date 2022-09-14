from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Groceryitem

def index(request):
    floofy = Groceryitem.objects.all()
    context = {'grocery_list': floofy}
    return render(request, 'grocery_app/index.html', context)

def delete(request, id):
    item = Groceryitem.objects.get(id = id)
    item.delete()
    return redirect('/')

def complete(request, id):
    item = Groceryitem.objects.get(id = id)
    item.complete = True
    item.date_completed = timezone.now()
    item.save()
    return redirect('/')

def undo(request, id):
    item = Groceryitem.objects.get(id = id)
    item.complete = False
    item.date_completed = None
    item.save()
    return redirect('/')

def add(request):
    if request.method == 'POST':
        item_description = request.POST.get('new_item')
        Groceryitem.objects.create(text_description = item_description)
    return redirect('/')