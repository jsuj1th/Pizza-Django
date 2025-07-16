from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
# Create your views here.
def home(request):
    return render(request, "pizza/home.html")


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()  # Save the pizza order to the database
            # Process the order here
            note="Your order has been placed successfully! your %s %s and %s pizza is on the way" % (filled_form.cleaned_data['size'], filled_form.cleaned_data['topping1'], filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            return render(request, "pizza/order.html", {"pizza_form": new_form, "note": note, "multiple_form": multiple_form})
    else:
        form = PizzaForm()
    return render(request, "pizza/order.html", {"pizza_form": form, "multiple_form": multiple_form})
    # if request.method == "POST":
    #     # Process the order here
    #     return render(request, "pizza/order_success.html")
    # else:
    #     return render(request, "pizza/order_form.html")

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_form = MultiplePizzaForm(request.GET)
    if filled_multiple_form.is_valid():
        number_of_pizzas = filled_multiple_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset=PizzaFormSet()
    if request.method == "POST":
        formset = PizzaFormSet(request.POST)
        if formset.is_valid():
            # Process the order here
            note = "Your order has been placed successfully!"
            return render(request, "pizza/pizzas.html", {"formset": formset, "note": note})
        else:
            note = "Please correct the errors below."
            return render(request, "pizza/pizzas.html", {"formset": formset, "note": note})
    else:
        return render(request, "pizza/pizzas.html", {"formset": formset})