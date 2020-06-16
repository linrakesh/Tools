from django.urls import path
from .views import qr_code_generator

urlpatterns = [
    path('qrcode/', qr_code_generator, name="qrcode"),
]
