from django.urls import path
from . import views
from .views import SignUpView




urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # path("autheticate/", views.authenticate),
    path("token_response/", views.token_response),
]