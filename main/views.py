from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def packages(request):
    return render(request, 'main/packages.html')

def customers(request):
    return render(request, 'main/customers.html')

def start_hosting(request):
    return render(request, 'main/start-hosting.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')