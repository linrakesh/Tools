from django.shortcuts import render

# Create your views here.


def qr_code_generator(request):
    if request.method == 'POST':
        data = request.POST['name']
        # print(data)
        return render(request, 'tools/generate_qr.html', {'data': data})
    else:
        return render(request, 'tools/generate_qr.html')
