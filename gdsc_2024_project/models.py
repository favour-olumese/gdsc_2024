from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    publisher = models.ForeignKey('Publisher', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.book_name
    
class author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class publisher(models.Model):
    pub_name = models.CharField(max_length=300)

    def __str__(self):
        return self.pub_name
