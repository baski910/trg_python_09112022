from django.db import models

# Create your models here.

class Book(models.Model):
    booktitle = models.CharField(max_length=50)
    bookauthor = models.CharField(max_length=50)

    def __str__(self):
        return f"Title:{self.booktitle},Author:{self.bookauthor}"
