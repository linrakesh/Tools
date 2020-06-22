from django.urls import path
from .views import shorturl_home

urlpatterns = [
    path('shorturl', shorturl_home, name="short_home"),

]
