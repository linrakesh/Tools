from django.urls import path
from .views import decimal_to_binary,string_to_binary,binary_to_decimal

urlpatterns = [
    path('decimal_binary/', decimal_to_binary, name="decimal_2_binary"),
    path('string_binary/', string_to_binary, name="string_2_binary"),
    path('binary_decimal/', binary_to_decimal, name="binary_2_decimal"),
]
