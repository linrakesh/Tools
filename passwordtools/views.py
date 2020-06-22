from django.shortcuts import render

# Create your views here.
import random


def password_generator(request):
    if request.method == 'POST':
        length = int(request.POST['length'])
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
        password = ""
        for i in range(length+1):
            password += random.choice(chars)
        print(password)
        return render(request, 'passwordtools/password_gen.html', {'password': password})
    else:
        return render(request, 'passwordtools/password_gen.html')


def password_strength(request):
    return render(request, 'passwordtools/password_strength.html')
