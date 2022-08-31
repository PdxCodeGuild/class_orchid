from re import template
from django.shortcuts import render

from django.http import HttpResponse

from .models import groceryitem

from django.template import loader
"""
def index(request):
    full_grocery_list = groceryitem.objects
    template = loader.get_template("grocerylist/index.html")
    context = {full_grocery_list: full_grocery_list,}
    return HttpResponse(template.render(context, request))
"""

def index(request):
    full_grocery_list = groceryitem.objects.order_by('-pub_date')[:5]
    context = {'full_grocery_list': full_grocery_list, }
    return render(request, 'grocerylist/index.html', context)