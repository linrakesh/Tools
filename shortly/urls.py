from django.urls import path
from .views import shorturl_home, short_url_redirect

urlpatterns = [
    path('shorturl', shorturl_home, name="short_home"),
    path('<str:query>/', short_url_redirect, name="short_redirect"),
]
