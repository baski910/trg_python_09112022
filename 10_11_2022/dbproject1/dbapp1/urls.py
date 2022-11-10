from django.urls import path
from . import views

urlpatterns = [
    path('books',views.books,name='books'),
    path('addbook',views.addbook,name='addbook')
]