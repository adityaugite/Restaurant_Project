from django.contrib import admin
from django.urls import path
from Aditya import views

urlpatterns = [
    path("", views.index, name='home'),
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contactus'),
    path('order/', views.ordernow, name='ordernow'),
    
]

