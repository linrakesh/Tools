from django.urls import path
from .views import decimal_to_binary

urlpatterns = [
    path('decimal_binary/', decimal_to_binary, name="decimal_2_binary"),
]
