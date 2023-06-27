from django.urls import path
from notice import views

urlpatterns = [
    path('', views.notice, name='notice'),
    path('create_n/', views.create_n, name='create_n'),
    path('post_detail_n/<int:id>/', views.post_detail_n, name='post_detail_n'),
    path('update_n/<int:id>/', views.post_update_n, name='post_update_n'),
    path('delete_n/<int:id>/', views.post_delete_n, name='post_delete_n'),
]