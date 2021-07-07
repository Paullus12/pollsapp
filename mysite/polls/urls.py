from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('created', views.created, name = 'created'),
    path('create/', views.create),
    path('completed', views.completed)
]