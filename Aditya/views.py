from django.shortcuts import render, HttpResponse, redirect

from .models import OrderNow, FoodItem
from .forms import OrderNowForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import OrderNow, FoodItem
from .serializers import OrderNowSerializer, FoodItemSerializer

# Home page view
def index(request):
    return render(request, 'home.html')

# About Us page view
def aboutus(request):
    return render(request, 'aboutus.html')

# Contact Us page view
def contactus(request):
    return render(request, 'contactus.html')

def ordernow(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        married = request.POST.get('married') == 'True'
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        food_items_names = request.POST.getlist('food_items')  # Retrieve the names of the food items
  
        
        order = OrderNow(
            name=name,
            email=email,
            dob=dob,
            age=age,
            married=married,
            gender=gender,
            location=location
        )
        order.save()

        
        food_items = FoodItem.objects.filter(name__in=food_items_names)  # Filter by names

        order.food_items.set(food_items)

        return redirect('home')  
        
        return render(request, 'order_success.html')

    
    return render(request, 'ordernow.html')


def order_list(request):
    
    location = request.GET.get('location')
    age_filter = request.GET.get('age')

    
    orders = OrderNow.objects.all()

    
    if location:
        orders = orders.filter(location=location)

    
    if age_filter == '35+':
        orders = orders.filter(age__gt=35)

    
    return render(request, 'order_list.html', {'orders': orders})



# Retrieve all orders or create a new order
@api_view(['GET', 'POST'])
def orders_list(request):
    if request.method == 'GET':
        orders = OrderNow.objects.all()
        serializer = OrderNowSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderNowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a single order
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def order_detail(request, pk):
    try:
        order = OrderNow.objects.get(pk=pk)
    except OrderNow.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderNowSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderNowSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = OrderNowSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
