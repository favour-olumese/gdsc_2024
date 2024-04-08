from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.

from .models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ['author', 'book_name', 'publisher']

admin.site.register(Book, BookAdmin)