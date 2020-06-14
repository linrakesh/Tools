from django import forms
from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
import csv
import json
import whois


def home(request):
    return render(request, 'tools/home.html')


def csv_to_json(csv_data):

    count = 1
    keys = []
    data = []
    for row in csv_data:
        if count == 1:
            for key in row:
                keys.append(key)
        else:
            element = {}
            for x in range(len(row)):
                element[keys[x]] = row[x]
        data.append(element)
        count += 1

    return json.dumps(data)


def convert_into_json(csv_file):
    li = csv_file.split('\r\n')
    n = len(li)
    count = 1
    keys = []
    data = []
    for row in li:
        if count == 1:
            for key in row.split(','):
                keys.append(key)
        else:
            element = {}
            words = row.split(',')
            for value in range(len(row.split(','))):
                element[keys[value]] = words[value]
            data.append(element)

        count = count+1

    return json.dumps(data,)


def tool(request):
    if request.method == 'POST':
        data = request.POST['csv_data']
        """ try:
            uploaded_file = request.FILES['myFile']
            binary_data = uploaded_file.read()
            data = binary_data
            json_data = binary_data
        except: """
        json_data = convert_into_json(data)

        #json_data = "data is coming from file"
        return render(request, 'tools/csv_to_json.html', {'csv': data, 'json': json_data})
    else:
        return render(request, 'tools/csv_to_json.html')

# function that convert csv data into html table and return to
# its calling function


def convert_into_html(csv_file):
    li = csv_file.split('\r\n')
    n = len(li)
    count = 1
    html = "<table>"
    for row in li:
        html += "<tr>"
        if count == 1:
            for y in row.split(','):
                html += "<th>"+y+"</th>"
        else:
            for y in row.split(','):
                html += "<td>"+y+"</td>"
        html += "</tr>"
        count += 1

    html += "</table>"
    return html


def csv_html(request):
    if request.method == 'POST':
        data = request.POST['csv_data']
        html_data = convert_into_html(data)
        return render(request, 'tools/csv_to_html.html', {'csv': data, 'html_data': html_data})
    else:
        return render(request, 'tools/csv_to_html.html')

# python view to convert CSV data into XML data


def convert_into_xml(csv_file):

    xml = '<?xml version= "1.0" encoding="UTF-8" ?><rows>'
    keys = []
    li = csv_file.split('\r\n')
    n = len(li)
    count = 1
    for row in li:
        if count == 1:
            for y in row.split(','):
                keys.append(y)
        else:
            xml += "<row>"
            for y in range(len(row.split(','))):
                xml += "<"+keys[y]+">"+row[y]+"</"+keys[y]+">"
            xml += "</row>"
        count += 1

    xml += "</rows>"
    return xml


def csv_xml(request):
    if request.method == 'POST':
        data = request.POST['csv_data']
        xml_data = convert_into_xml(data)
        return render(request, 'tools/csv_to_xml.html', {'csv': data, 'xml_data': xml_data})
    else:
        return render(request, 'tools/csv_to_xml.html')


def handle_uploaded_file(f):
    destination = open('c:/%s' % f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


def resize_images(request):
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        # print(files)
        for f in files:
            if f.size > 5*1024*1024:
                raise forms.ValidationError("File is too big.")

        return render(request, "tools/resize_files.html", {'files': files})
    else:
        return render(request, "tools/resize_files.html")


def temp_converter(request):
    if request.method == 'POST':
        cel = request.POST['cel']
        temp = eval(cel)
        if(type(cel) == int or type(cel) == float):
            fah = (temp+32)*9/5
            return render(request, "tools/temp_conversion.html", {'cel': cel, 'fah': fah})
        else:
            return render(request, "tools/temp_conversion.html", {'cel': cel, 'fah': 'invalid Data type'})
    else:
        return render(request, "tools/temp_conversion.html")


def tool_request(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name, email, message)
        return render(request, "tools/thanks.html")
    else:
        return render(request, "tools/request.html")


def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['message']

        subject = "Contact us Email From Django App -" + name
        send_mail(subject, msg, email, [
                  'rakesh@binarynote.com'], fail_silently=False)
        return render(request, "tools/thanks.html")
    else:
        return render(request, "tools/contact.html")


def qr_code_generator(request):
    if request.method == 'POST':
        data = request.POST['name']
        # print(data)
        return render(request, 'tools/generate_qr.html', {'data': data})
    else:
        return render(request, 'tools/generate_qr.html')
