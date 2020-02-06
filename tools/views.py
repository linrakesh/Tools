from django.shortcuts import render


# Create your views here.
import csv
import json


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


def convert_into_html(data):
    return data


def csv_html(request):
    if request.method == 'POST':
        data = request.POST['csv_data']
        html_data = convert_into_html(data)
        return render(request, 'tools/csv_to_html.html', {'csv': data, 'html_data': html_data})
    else:
        return render(request, 'tools/csv_to_html.html')


def temp_converter(request):
    if request.method == 'POST':
        cel = int(request.POST['cel'])
        fah = (cel+32)*9/5
        return render(request, "tools/temp_conversion.html", {'cel': cel, 'fah': fah})
    else:
        return render(request, "tools/temp_conversion.html")


def tool_request(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name, email, message)
        return render(request, "tools/temp_conversion.html")
    else:
        return render(request, "tools/request.html")


def contact_us(request):
    return render(request, "tools/contact.html")
