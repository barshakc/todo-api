from django.urls import path
from .api import views

urlpatterns=[
    path(route='list/',view=views.ToDoAPIListView.as_view(),name='create'),
    path(route='list/<int:pk>/',view=views.ToDoAPIDetailView.as_view(),name='edit'),

]