from datetime import date
from django.shortcuts import render

# Create your views here.
import whois
import datetime


def url_age(url):
    domain = whois.whois(url)

    cur_year = date.today().year
    cur_month = date.today().month
    cur_day = date.today().day

    creation_date = str(domain['creation_date']).split()[0]
    creat_year = int(creation_date.split('-')[0])
    creat_month = int(creation_date.split('-')[1])
    creat_day = int(creation_date.split('-')[2])

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if cur_day < creat_day:
        cur_day += month[cur_month-1]
        cur_month = cur_month-1

    if cur_month < creat_month:
        cur_month = cur_month+12
        cur_year = cur_year-1

    year = cur_year-creat_year
    month = cur_month-creat_month
    day = cur_day-creat_day

    age = {'year': year, 'month': month, 'day': day}
    return age


def domain_age(request):
    if request.method == 'POST':
        url = request.POST['domain']
        age = url_age(url)
        return render(request, 'domaintools/domain_age.html', {'age': age})
    else:
        return render(request, 'domaintools/domain_age.html')


def whois_data(request):
    if request.method == 'POST':
        domain_name = request.POST['name']
        domain = whois.whois(domain_name)
        return render(request, 'domaintools/whois.html', {'domain': domain})
    else:
        return render(request, 'domaintools/whois.html')
