from django.shortcuts import render

# Create your views here.


def int_binary(no):
    binary = ''
    while no != 0:
        binary = binary+str(no % 2)
        no = no//2
    return binary[::-1]

def float_binary(no):
    binary = ''
    steps = 0
    while steps <= 5 and no != 0.0:
        no = no*2
        rem = int(no)
        binary = binary + str(rem)
        if rem >= 1:
            no = no-1.0
        steps = steps+1

    return binary

def decimal_to_binary(request):
    if request.method=='POST':
        dec = request.POST['decimal']
        int_no = int(float(dec))
        float_no = float(dec)
        diff = float_no - int_no
        if diff > 0.0:
            no = int_binary(int_no) + "." + float_binary(diff)
            #print(no)
        else:
            no = int_binary(int_no)
        return render(request,'binarytools/decimal_2_binary.html',{'no':no,'decimal':dec})
    else:
        return render(request, 'binarytools/decimal_2_binary.html')


def string_to_binary(request):
    if request.method=='POST':
        string = request.POST['string']
        binarycode = ''
        for x in string:
            binarycode = binarycode + ' ' + int_binary(ord(x))
        return render(request,'binarytools/string_2_binary.html',{'no':binarycode,'string':string})
    else:
        return render(request,'binarytools/string_2_binary.html')


def binary_to_decimal(request):
    if request.method == 'POST':
        n = int(request.POST['binary'])
        sum1 = 0
        i = 0
        while n != 0:
            rem = n % 10
            sum1 = sum1+rem*2**i
            n = n//10
            i = i+1
        return render(request, 'binarytools/binary_2_decimal.html', {'no': sum1, 'binary': n})
    else:
        return render(request, 'binarytools/binary_2_decimal.html')


def decimal_to_octal(request):
    if request.method == 'POST':
        no = int(request.POST['decimal'])
        octal = ''
        while no != 0:
            rem = no % 8
            if rem == 0:
                octal = octal+'0'
            if rem == 1:
                octal = octal+'1'
            if rem == 2:
                octal = octal+'2'
            if rem == 3:
                octal = octal+'3'
            if rem == 4:
                octal = octal+'4'
            if rem == 5:
                octal = octal+'5'
            if rem == 6:
                octal = octal+'6'
            if rem == 7:
                octal = octal+'7'
            no = no // 8
         
        return render(request, 'binarytools/decimal_2_octal.html', {'no': octal[::-1], 'decimal':no })
    else:
        return render(request, 'binarytools/decimal_2_octal.html')
