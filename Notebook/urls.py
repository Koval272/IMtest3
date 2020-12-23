from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('view/', views.check),
    path('add/', views.add),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
]
