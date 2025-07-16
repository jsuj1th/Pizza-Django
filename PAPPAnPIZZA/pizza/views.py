from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.
def home(request):
    return render(request, "pizza/home.html")


def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            # Process the order here
            note="Your order has been placed successfully! your %s %s and %s pizza is on the way" % (filled_form.cleaned_data['size'], filled_form.cleaned_data['Topping1'], filled_form.cleaned_data['Topping2'])
            new_form = PizzaForm()
            return render(request, "pizza/order.html", {"pizza_form": new_form, "note": note})
    else:
        form = PizzaForm()
    return render(request, "pizza/order.html", {"pizza_form": form})
    # if request.method == "POST":
    #     # Process the order here
    #     return render(request, "pizza/order_success.html")
    # else:
    #     return render(request, "pizza/order_form.html")