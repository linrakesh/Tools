from django.urls import path
from .views import decimal_to_binary, string_to_binary, binary_to_decimal, decimal_to_octal, decimal_to_hexa, binary_to_octal, binary_to_hexa, hexadecimal_to_decimal

urlpatterns = [
    path('decimal_binary/', decimal_to_binary, name="decimal_2_binary"),
    path('string_binary/', string_to_binary, name="string_2_binary"),
    path('binary_decimal/', binary_to_decimal, name="binary_2_decimal"),
    path('hexa_decimal/', hexadecimal_to_decimal, name="hexa_2_decimal"),
    path('binary_octal/', binary_to_octal, name="binary_2_octal"),
    path('binary_hexa/', binary_to_hexa, name="binary_2_hexa"),
    path('decimal_octal/', decimal_to_octal, name="decimal_2_octal"),
    path('decimal_hexa/', decimal_to_hexa, name="decimal_2_hexa"),
]
