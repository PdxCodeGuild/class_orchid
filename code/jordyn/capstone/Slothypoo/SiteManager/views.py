from django.shortcuts import render
from django.urls import reverse
from .forms import ImageForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def image_upload_view(request):
    admin_obj = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'SiteManager.html', {'form': form, 'img_obj': img_obj, 'admin_obj': admin_obj,})
    else:
        form = ImageForm()
    return render(request, 'SiteManager.html', {'form': form, 'admin_obj': admin_obj,})

@login_required
def image_delete(request, id): #gonna delete sum stuff
    image = Image.objects.get(id=id)
    image.delete()
    return HttpResponseRedirect(reverse('SiteManager'))