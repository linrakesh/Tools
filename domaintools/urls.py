from django.urls import path
from .views import domain_age, whois_data

urlpatterns = [
    path('domain_age/', domain_age, name="domain_age"),
    path('whois/', whois_data, name="whois"),
]
