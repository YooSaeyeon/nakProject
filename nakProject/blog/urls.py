from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create_b/', views.create_b, name='create_b'),
    path('post_detail_b/<int:id>/', views.post_detail_b, name='post_detail_b'),
    path('update_b/<int:id>/', views.post_update_b, name='post_update_b'),
    path('delete_b/<int:id>/', views.post_delete_b, name='post_delete_b'),
    path('create_comment_b/<int:id>', views.create_comment_b, name='create_comment_b'),
    path('update_comment_b/<int:blogPost_id>/<int:com_id>', views.update_comment_b, name='update_comment_b'),
    path('delete_comment/<int:blogPost_id>/<int:com_id>', views.delete_comment_b, name='delete_comment_b')
]