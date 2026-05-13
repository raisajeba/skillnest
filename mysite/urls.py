from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path(
        '',
        TemplateView.as_view(
            template_name='home.html'
        ),
        name='home'
    ),

    path(
        'skills/',
        include('skills.urls')
    ),

    path(
        'account/',
        include('accounts.urls')
    ),

    path(
        'exchange/',
        include('exchanges.urls')
    ),
    path(
    'ratings/',
    include('ratings.urls')
    ),

    path(
        'admin/',
        admin.site.urls
    ),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)