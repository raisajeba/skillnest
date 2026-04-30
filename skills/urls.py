from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skill/<int:pk>/', views.skill_detail, name='skill_detail'),
    path('add/', views.add_skill, name='add_skill'),
    path('update/<int:pk>/', views.update_skill, name='update_skill'),
    path('delete/<int:pk>/', views.delete_skill, name='delete_skill'),
]