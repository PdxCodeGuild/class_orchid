from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('index/', views.IndexView.as_view(), name="index"),
    path('<str:username>/', views.UserProfileView.as_view(), name="profile")
]

# inside of each app the project urls are used to direct users to app urls and the app urls directs to the views of that specfic app