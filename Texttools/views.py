from django.shortcuts import render

# Create your views here.


def word_count(request):
  if request.method=='POST':
    data = request.POST['text']
    n = len(data)
    list1 = data.split()
    words = len(data.split())
    vowels=conso=upper=lower=digit=medium =large=short=0
    for x in data: 
      if x in 'AEIOUaeiou':
        vowels +=1
      else:
        conso+=1 
      if x.isupper():
        upper +=1
      elif x.islower():
        lower+=1  
      elif x.isdigit():
        digit+=1
    for x in list1:
        if len(x)<=4:
           short+=1
        if len(x)>=6 and len(x)<=10:
           medium+=1
        if len(x)>10:
           large+=1
    uppercase = data.upper()
    lowercase = data.lower()

    result ={'chars':n, 'words': words,'vowels':vowels,'conso':conso,'upper':upper,'lower':lower,
             'digit':digit,'short':short,'medium':medium,'large':large,'uppercase':uppercase,'lowercase':lowercase,
            }
    
    return render(request, 'Texttools/word_count.html',{'summery':result})
  else:
    return render(request, 'Texttools/word_count.html')
