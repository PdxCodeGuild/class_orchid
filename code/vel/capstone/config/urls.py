from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', include('exercise.urls')),
    path('planner/', include('planner.urls')),
    # path('', TemplateView.as_view(template_name='base.html'), name='base'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
