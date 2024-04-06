from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Book

# Create your views here.
def fav(request):
    return JsonResponse({'Expectation': 'Looking forward to great things.'})

def home(request):
    return render(request, 'gdsc_2024_project/home.html')

def home_api(request):
    return JsonResponse({'message': 'Hello GDSC'})


class BookCreateView(CreateView):
    model = Book
    fields = ["book_name"]

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("book-list")

class BookUpdateView(UpdateView):
    model = Book
    fields = ["book_name"]

class BookListView(ListView):
    model = Book