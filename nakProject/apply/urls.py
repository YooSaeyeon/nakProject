from django.urls import path
from apply import views

urlpatterns = [
    path('', views.apply, name='apply'),
    #path('create/', views.create, name='create'),
]