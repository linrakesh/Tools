from django.shortcuts import render,redirect
from .models import shorturl
import random
import string


def generate_short_url():
    while True:
        url = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
        check = shorturl.objects.filter(short_url = url)
        if not check:
            break
    return url 

def shorturl_home(request):
    if request.method =='POST':
        url = request.POST['url']
        shortname = request.POST['custom']
        if len(shortname)==0: 
            newshort_url = generate_short_url()
            newurl = shorturl(original_url=url, short_url=newshort_url)
        else:
            check = shorturl.objects.filter(short_url = shortname)
            if not check:
               newurl = shorturl(original_url = url,short_url=url)
             
        newurl.save()
      
    urls = shorturl.objects.all()[:10]
    return render(request, 'shortly/home.html', {'urls': urls})
   

def short_url_redirect(request,query):
    if not query or query is None:
        return render(request, 'shortly/home.html')
    else:
        try:
            check = shorturl.objects.get(short_url=query)
            url_to_redirect = check.original_url
            return redirect(url_to_redirect)
        except shorturl.DoesNotExist:
            return render(request, 'shortly/home.html', {'error': "error"})
