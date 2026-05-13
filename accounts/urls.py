from django.urls import path
from . import views

from django.contrib.auth.views import (
    LoginView,
    LogoutView
)


urlpatterns = [

    path(
        'signup/',
        views.signup,
        name='signup'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(
            next_page='login'
        ),
        name='logout'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'profile/edit/',
        views.edit_profile,
        name='edit_profile'
    ),

    path(
        'skill/add/',
        views.add_skill,
        name='add_skill'
    ),

    path(
        'skill/edit/<int:pk>/',
        views.edit_skill,
        name='edit_skill'
    ),

    path(
        'skill/delete/<int:pk>/',
        views.delete_skill,
        name='delete_skill'
    ),
]