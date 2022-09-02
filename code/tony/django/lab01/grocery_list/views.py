from datetime import datetime
from django.shortcuts import render
from re import match

from .models import GroceryItem

def index(request):
    grocery_list = GroceryItem.objects.order_by('-creation_date')[:5]   
    context = { 'grocery_list': grocery_list }
    description = request.POST.get('description')
    delete = ''.join([m.groups()[0] for m in [match('delete(\d+)', field) for field in request.POST] if not m == None])
    complete = ''.join([m.groups()[0] for m in [match('complete(\d+)', field) for field in request.POST] if not m == None])
    incomplete = ''.join([m.groups()[0] for m in [match('incomplete(\d+)', field) for field in request.POST] if not m == None])
    if description:
        GroceryItem(description=description, creation_date=datetime.now(), is_complete=b'0').save()
    if delete:
        GroceryItem.objects.get(id=delete).delete()
    if complete:
        g = GroceryItem.objects.get(id=complete)
        g.completed_date = datetime.now()
        g.is_complete = b'1'
        g.save()
    if incomplete:
        g = GroceryItem.objects.get(id=incomplete)
        g.completed_date = None
        g.is_complete = b'0'
        g.save()
    for item in grocery_list:
        if item.is_complete == b'1':
            item.is_complete = True
            item.description = f'<strike>{item.description}</strike>'
        else:
            item.is_complete = False
    return render(request, 'grocery_list/index.html', context)
