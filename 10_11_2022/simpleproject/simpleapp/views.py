from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# reverse('simpleapp:index')

def index(request):
    #return HttpResponse("<h1>Welcome to Django app</h1>")
    return render(request,"simpleapp/welcome.html")
