from django.shortcuts import render

# Create your views here.
def decimal_to_binary(request):
    return render(request,'binarytools/decimal_2_binary.html')