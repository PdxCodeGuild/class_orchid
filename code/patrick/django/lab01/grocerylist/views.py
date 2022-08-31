from re import template
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import GroceryItem

from django.template import loader
"""
def index(request):
    full_grocery_list = groceryitem.objects
    template = loader.get_template("grocerylist/index.html")
    context = {full_grocery_list: full_grocery_list,}
    return HttpResponse(template.render(context, request))
"""

def index(request):
    if request.method == "POST":
        item_text = request.POST.get("item_text")
        GroceryItem.objects.create(
            item_text = item_text

        )
        return redirect("/")









    full_grocery_list = GroceryItem.objects.all()
    context = {
        'full_grocery_list': full_grocery_list,
    }
    return render(request, 'grocerylist/index.html', context)