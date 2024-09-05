from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class OrderNow(models.Model):
    LOCATION_CHOICES = [
        ('City', 'City'),
        ('Village', 'Village'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    age = models.PositiveIntegerField()
    married = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES)
    image = models.ImageField(upload_to='customer_images/', blank=True, null=True)
    food_items = models.ManyToManyField(FoodItem)

    def __str__(self):
        return self.name
