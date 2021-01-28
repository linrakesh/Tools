from django.shortcuts import render

# Create your views here.


def word_count(request):
  if request.method=='POST':
    data = request.POST['text']
    n = len(data)
    words = len(data.split())
    vowels=0;
    conso=0
    upper=lower=digit=0
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
    result ={'chars':n, 'words': words,'vowels':vowels,'conso':conso,'upper':upper,'lower':lower,'digit':digit}
    return render(request, 'Texttools/word_count.html',{'summery':result})
  else:
    return render(request, 'Texttools/word_count.html')
