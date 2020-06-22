from django.shortcuts import render
from .models import shorturl
# Create your views here.


def shorturl_home(request):
    urls = shorturl.objects.all()
    return render(request, 'shortly/home.html', {'u': urls})
