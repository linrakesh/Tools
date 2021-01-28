from django.urls import path
from .views import word_count

urlpatterns = [
    path('wordcount/', word_count, name="word_count"),
    
]
