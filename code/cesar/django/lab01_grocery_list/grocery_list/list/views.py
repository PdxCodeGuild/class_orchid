from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the List Index.")


def grocery_list(request, item_id):
    return HttpResponse(f"Welcome {item_id}")
