from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=150)
    book_name = models.CharField(max_length=200)
    publisher = models.CharField(max_length=350)

    def __str__(self):
        return self.book_name
    
    def get_absolute_url(self):
        return reverse("book-list")