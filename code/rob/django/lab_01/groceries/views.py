from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import GroceryItem

# Create your views here.
def index(request):
    if request.method == 'POST':
        text_description = request.POST.get('text_description')
        created_date = timezone.now()
        GroceryItem.objects.create(
            text_description = text_description,
            created_date = created_date,
        )
        return redirect('/')

    latest_grocery_list = GroceryItem.objects.order_by('-created_date')[:5]
    context = {'latest_grocery_list': latest_grocery_list}
    return render(request, 'groceries/index.html', context)


def detail(request, item_id):
    try:
        item = GroceryItem.objects.get(pk=item_id)
    except GroceryItem.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'groceries/detail.html', {'item': item})


def delete(request, item_id):
    item = GroceryItem.objects.get(pk=item_id)
    item.delete()
    return redirect('/')


def completed(request, item_id):
    item_completed = GroceryItem.objects.get(pk=item_id)
    item_completed.completed = True
    item_completed.completed_date = timezone.now()
    item_completed.save()
    return redirect('/')


def undo(request, item_id):
    item_completed = GroceryItem.objects.get(pk=item_id)
    item_completed.completed = False
    item_completed.completed_date = None
    item_completed.save()
    return redirect('/')