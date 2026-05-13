from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.ratings_home,
        name='ratings_home'
    ),

    path(
        'give/<int:user_id>/',
        views.give_rating,
        name='give_rating'
    ),

]