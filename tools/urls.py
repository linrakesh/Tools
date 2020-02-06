from django.urls import path
from .views import tool, temp_converter, tool_request, contact_us

urlpatterns = [
    path('', tool, name="csv_to_json"),
    path('temp/', temp_converter, name="temp_convert"),
    path('request/', tool_request, name="tool_request"),
    path('contact/', contact_us, name="contact_us"),
]
