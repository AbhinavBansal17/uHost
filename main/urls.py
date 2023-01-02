from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('packages', views.packages, name="packages"),
    path('customers', views.customers, name="customers"),
    path('start-hosting', views.start_hosting, name="start-hosting"),
    path('portfolio', views.portfolio, name="portfolio")
]