from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def fav(request):
    return JsonResponse({'Expectation': 'Looking forward to great things.'})

def home(request):
    return render(request, 'gdsc_2024_project/home.html')

def home_api(request):
    return JsonResponse({'message': 'Hello GDSC'})
