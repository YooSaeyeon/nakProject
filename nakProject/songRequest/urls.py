from django.urls import path
from songRequest import views

urlpatterns = [
    path('', views.songRequest, name='songRequest'),
    path('create_s/', views.create_s, name='create_s'),
    path('post_detail_s/<int:id>/', views.post_detail_s, name='post_detail_s'),
    path('update_s/<int:id>/', views.post_update_s, name='post_update_s'),
    path('delete_s/<int:id>/', views.post_delete_s, name='post_delete_s'),
]