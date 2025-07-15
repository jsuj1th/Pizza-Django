from django import forms

class PizzaForm(forms.Form):
    Topping1 = forms.CharField(label="Topping1", max_length=100)
    Topping2 = forms.CharField(label="Topping2", max_length=100)
    size = forms.ChoiceField(label="Size", choices=[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ])
    