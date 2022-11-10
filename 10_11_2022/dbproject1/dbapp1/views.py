from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Book
from .forms import BookForm
# Create your views here.

def books(request):
    books = Book.objects.all()
    return render(request,"dbapp1/books.html",{'books':books})

def addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('dbapp1:books'))
    else:
        form = BookForm()
        return render(request,"dbapp1/addbook.html",{'form': form})
    