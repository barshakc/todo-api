from django.urls import path
from .api import views

urlpatterns=[
    path(route='list/',view=views.ToDoAPIListView.as_view(),name='create'),
    path(route='list/<int:pk>/',view=views.ToDoAPIDetailView.as_view(),name='edit'),
    path('register/',view= views.UserRegistration.as_view(), name='register'),
    path('login/', view= views.UserLoginView.as_view(), name='login'),

]