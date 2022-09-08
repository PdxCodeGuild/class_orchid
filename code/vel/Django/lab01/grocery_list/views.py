from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.utils import timezone

# from models I imported the name of my model(s) ex: GroceryList
from .models import GroceryItem


def index(request):
    # latest_grocery_list = GroceryItem.objects.order_by('-created_date')
    # template =loader.get_template('grocery_list/index.html')
    latest_grocery_list = GroceryItem.objects.filter(completed=False)
    completed_grocery_list = GroceryItem.objects.filter(completed=True)
    grocery_list = GroceryItem.objects.all()
    for item in grocery_list:
        print(item.id)
    context = {
        'latest_grocery_list': latest_grocery_list,
        'completed_grocery_list': completed_grocery_list,
        'grocery_list': grocery_list
    }
    return render(request, 'index.html', context)


def add_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        created_date = timezone.now()
        GroceryItem.objects.create(
            item_name=item_name,
            created_date=created_date
        )
    return redirect('index')


# shortcut would be to add .delete() to the end of line 25
def remove_item(request, item_id):
    this_item = get_object_or_404(GroceryItem, id=item_id)
    this_item.delete()
    print(item_id)
    return redirect('index')


# redirect back to my home page which is "index"
def complete(request, item_id):
    this_item = get_object_or_404(GroceryItem, id=item_id)
    this_item.completed = True
    this_item.completed_date = timezone.now()
    this_item.save()
    return redirect('index')


def incomplete(request, item_id):
    this_item = get_object_or_404(GroceryItem, id=item_id)
    this_item.completed = False
    this_item.save()
    return redirect('index')
