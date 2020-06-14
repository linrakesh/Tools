from django.urls import path
from .views import decimal_to_binary,string_to_binary,binary_to_decimal,decimal_to_octal,decimal_to_hexa,binary_to_octal

urlpatterns = [
    path('decimal_binary/', decimal_to_binary, name="decimal_2_binary"),
    path('string_binary/', string_to_binary, name="string_2_binary"),
    path('binary_decimal/', binary_to_decimal, name="binary_2_decimal"),
    path('binary-octal/', binary_to_octal, name="binary_2_octal"),
    path('decimal-octal/', decimal_to_octal, name="decimal_2_octal"),
    path('decimal-hexa/', decimal_to_hexa, name="decimal_2_hexa"),
]
