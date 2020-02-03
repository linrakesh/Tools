from django.urls import path
from .views import tool

urlpatterns = [
    path('', tool, name="csv_to_json"),
]
