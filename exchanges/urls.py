
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exchange_home, name='exchange_home'),
    path('send/<int:skill_id>/', views.send_request, name='send_request'),
    path('action/<int:pk>/<str:action>/', views.request_action, name='request_action'),
    path('delete/<int:pk>/',views.delete_request,name='delete_request')
]