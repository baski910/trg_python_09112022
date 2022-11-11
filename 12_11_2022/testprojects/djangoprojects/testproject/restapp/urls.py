from django.urls import path, include
from .views import BookViews

urlpatterns = [
    path('books/',BookViews.as_view(),name="books")
]