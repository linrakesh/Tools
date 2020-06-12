from django.urls import path
from .views import domain_age

urlpatterns = [
    path('domain_age/', domain_age, name="domain_age"),
]
