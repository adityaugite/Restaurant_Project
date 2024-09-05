from django.shortcuts import render, HttpResponse, redirect

from .models import OrderNow, FoodItem
from .forms import OrderNowForm

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
        food_items_ids = request.POST.getlist('food_items')  
        
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

        
        food_items = FoodItem.objects.filter(id__in=food_items_ids)
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
