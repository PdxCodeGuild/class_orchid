
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('urlshortener/',include('urlshortener.urls')),
]
