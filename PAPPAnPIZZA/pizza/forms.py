from django import forms
from .models import Pizza, Size
# class PizzaForm(forms.Form):
#     Topping1 = forms.CharField(label="Topping1", max_length=100)
#     Topping2 = forms.CharField(label="Topping2", max_length=100)
#     size = forms.ChoiceField(label="Size", choices=[
#         ('small', 'Small'),
#         ('medium', 'Medium'),
#         ('large', 'Large'),
#     ])
    
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2',
            'size': 'Size'
        }
        