from django.shortcuts import HttpResponse

def sample(request):
    return HttpResponse("hello")
