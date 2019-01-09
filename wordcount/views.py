
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
     return render(request, 'home.html' )

def about(request):
    return render(request , 'about.html')

def eggs(request):
    return HttpResponse('<h1>Eggs are Great<h1>')

def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()
    wordlist_len = len(wordlist)
    wordlist_dict = {}


    for word in wordlist:
        if word in wordlist_dict:
            wordlist_dict[word] +=1
        else:
            wordlist_dict[word] = 1

    sortedwords = sorted(wordlist_dict.items(), key = operator.itemgetter(1), reverse = True)
    maximum = max([i for i in wordlist_dict.values()])

    return render(request , 'count.html',{'x':text,'y':wordlist_len,'z':wordlist_dict,'m':maximum, 'sortedwords' : sortedwords})
