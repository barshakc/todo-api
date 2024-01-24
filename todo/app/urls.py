from django.urls import path
from .api import views

urlpatterns=[
    path(route='list/',view=views.ToDoAPIView.as_view(),name='create'),

]