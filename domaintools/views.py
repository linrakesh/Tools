from django.shortcuts import render

# Create your views here.

def domain_age(request):
    if request.method =='POST':
        age = {'year':8,'month':1,'day':27}
        return render(request,'domaintools/domain_age.html',{'age':age})
    else:
        return render(request, 'domaintools/domain_age.html')
