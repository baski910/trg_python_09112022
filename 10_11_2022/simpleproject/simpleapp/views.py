from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# reverse('simpleapp:index')

def index(request):
    #return HttpResponse("<h1>Welcome to Django app</h1>")
    #msg = 'this is a test message from django application'
    #return render(request,"simpleapp/welcome.html",{'message': msg})
    #list_of_names =['bob','tom','pat','raj']
    #return render(request,"simpleapp/welcome.html",{'names': list_of_names})
    list_of_names =[{'name':'bob'},{'name':'tom'},{'name':'pat'},{'name':'raj'}]
    return render(request,"simpleapp/welcome.html",{'names': list_of_names})
