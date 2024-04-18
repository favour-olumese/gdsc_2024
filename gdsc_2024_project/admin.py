from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.

from .models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ['author', 'book_name', 'publisher']
    list_display = ['book_name', 'author', 'publisher']
    search_fields = ['book_name', 'author']

admin.site.register(Book, BookAdmin)