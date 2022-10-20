from django.urls import path

from . import views

urlpatterns = [
    path('', views.image_upload_view, name='SiteManager'),
    path('delete/<int:id>', views.image_delete, name='Delete')
]