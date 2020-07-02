from django.urls import path
from . import views

urlpatterns = [
    path('cv', views.cv, name='cv'),
    path('cv/education/new/', views.edu_new, name='edu_new'),
    path('cv/education/<int:pk>/edit/', views.edu_edit, name='edu_edit'),
    path('cv/education/<pk>/remove/', views.edu_remove, name='edu_remove'),
    path('cv/project/new/', views.proj_new, name='proj_new'),
    path('cv/project/<int:pk>/edit/', views.proj_edit, name='proj_edit'),
    path('cv/project/<pk>/remove/', views.proj_remove, name='proj_remove'),
    path('cv/experience/new/', views.exp_new, name='exp_new'),
    path('cv/experience/<int:pk>/edit/', views.exp_edit, name='exp_edit'),
    path('cv/experience/<pk>/remove/', views.exp_remove, name='exp_remove'),
    path('cv/certificate/new/', views.cert_new, name='cert_new'),
    path('cv/certificate/<int:pk>/edit/', views.cert_edit, name='cert_edit'),
    path('cv/certificate/<pk>/remove/', views.cert_remove, name='cert_remove'),
    path('cv/skill/new/', views.ski_new, name='ski_new'),
    path('cv/skill/<int:pk>/edit/', views.ski_edit, name='ski_edit'),
    path('cv/skill/<pk>/remove/', views.ski_remove, name='ski_remove'),
]
