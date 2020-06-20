from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('blog',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.blog_post, name='blog_post'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv', views.cv, name='cv'),

]
