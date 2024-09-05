from django import forms
from .models import OrderNow, FoodItem

class OrderNowForm(forms.ModelForm):
    food_items = forms.ModelMultipleChoiceField(
        queryset=FoodItem.objects.all(),  
        widget=forms.CheckboxSelectMultiple,  
        required=True  
    )

    class Meta:
        model = OrderNow  
        fields = ['name', 'email', 'dob', 'age', 'married', 'gender', 'location', 'image', 'food_items']

    def clean_food_items(self):
        selected_food_items = self.cleaned_data['food_items']  
        if len(selected_food_items) not in [2, 3, 5]: 
            raise forms.ValidationError('You must select exactly 2, 3, or 5 food items.')
        return selected_food_items  
