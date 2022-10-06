from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('add', views.add, name='add'),
    path('<int:question_id>/delete', views.delete, name='delete'),
    path('all_results/', views.all_results_view),
    path('api/all_questions', views.get_questions),
    path('api/all_choices', views.get_choices)
]
