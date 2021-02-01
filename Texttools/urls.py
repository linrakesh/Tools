from django.urls import path
from .views import word_count,md5_generator

urlpatterns = [
    path('wordcount/', word_count, name="word_count"),
    path('md5_generator/', md5_generator, name="md5"),
    
]
