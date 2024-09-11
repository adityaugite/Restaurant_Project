from django.contrib import admin
from django.urls import path
from Aditya import views
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contactus'),
    path('order/', views.ordernow, name='ordernow'),
    path('api/orders/', views.orders_list, name='orders-list'),
    path('api/orders/<int:pk>/', views.order_detail, name='order-detail'),
    
]



