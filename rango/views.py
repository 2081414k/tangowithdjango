from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #context_dict = {'boldmessage': "I am bold font from the context"}
    #return render(request, 'rango/index.html', context_dict)
    return HttpResponse("Rango says hey there world!")

def about(request):
    #context_dict2 = {'boldmessage': "Foivos Karounos"}
    #return render(request, 'rango/about.html', context_dict2)
    return HttpResponse("Foivos Karounos")