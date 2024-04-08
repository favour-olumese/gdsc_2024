"""
URL configuration for gdsc_2024 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import BookListView, BookUpdateView, BookDeleteView, BookCreateView

urlpatterns = [
    path('', views.fav, name='fav'),
    path('hello/', views.home, name='home'),
    path('api/hello/', views.home_api, name='home-api'),
    path("books/", BookListView.as_view(), name='book-list'),
    path("book/add/", BookCreateView.as_view(), name="book-add"),
    path("book/<int:pk>/", BookUpdateView.as_view(), name="book-update"),
    path("book/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
    path('register/', views.register, name='register')
]
