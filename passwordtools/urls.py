from django.urls import path
from .views import password_generator, password_strength

urlpatterns = [
    path('password_generator/', password_generator, name="password_generator"),
    path('password_strength/', password_strength, name="password_strength"),
]
