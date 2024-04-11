from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("book-list"))

def fav(request):
    return JsonResponse({'Expectation': 'Looking forward to great things.'})

def home(request):
    return render(request, 'gdsc_2024_project/home.html')

def home_api(request):
    return JsonResponse({'message': 'Hello GDSC'})


@login_required
@permission_required("admin", raise_exception=True)
def earnings(request):
    return render(request, 'gdsc_2024_project/earnings.html')



class BookCreateView(CreateView):
    model = Book
    fields = ['book_name', 'author', 'publisher']

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("book-list")

class BookUpdateView(UpdateView):
    model = Book
    fields = ['book_name', 'author', 'publisher']
    template_name = 'gdsc_2024_project/book_update_form.html'


class BookListView(LoginRequiredMixin, ListView):
    model = Book