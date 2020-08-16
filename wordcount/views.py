from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordlist = fulltext.split()
    worddict = dict()
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
#    sortword = sorted(worddict.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'fulltext': fulltext, \
            'count': len(wordlist), 'worddict':worddict.items()})
def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def pageA(request):
    return render(request, 'pageA.html')

def pageB(request):
    return render(request, 'pageB.html')
