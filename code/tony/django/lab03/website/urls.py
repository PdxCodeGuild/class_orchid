"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

# from chirps.models import Chirp

# from chirps import views

# chirps = Chirp.objects.all()
# userchirps = Chirp.objects.all()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('', include('chirps.urls')),
    path('<str:user>', include('chirps.urls')),
    # path('', views.HomeView.as_view(), name='home'),
    # path('<str:user>', views.UserView.as_view(), name='user'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home', kwargs={'chirps': chirps}),
    # path('<str:user>', TemplateView.as_view(template_name='user.html'), name='user', kwargs={'chirps': chirps}),
]
