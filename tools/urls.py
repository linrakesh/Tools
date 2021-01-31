from django.urls import path
from .views import (home, tool, csv_html, csv_xml, temp_converter, tool_request,
                    contact_us, resize_images, actual_resize_file,whatismyip,domain_name_generator)

urlpatterns = [
    path('', home, name="home"),
    path('csv2json', tool, name="csv_to_json"),
    path('csv2html/', csv_html, name="csv_to_html"),
    path('csv2xml/', csv_xml, name="csv_to_xml"),
    path('resize_images/', resize_images, name="resize_image"),
    path('resize_image_actual/', actual_resize_file, name="resize_images_actual"),
    path('domain_name/', domain_name_generator, name="domain_name"),
    path('myip/', whatismyip, name="myip"),

    path('temp/', temp_converter, name="temp_convert"),
    path('request/', tool_request, name="tool_request"),
    path('contact/', contact_us, name="contact_us"),
]
