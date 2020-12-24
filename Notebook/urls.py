from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('repairs/', views.index1),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('<int:audience>/', views.auF),
    path('<brand & model>/', views.brandF),
]
