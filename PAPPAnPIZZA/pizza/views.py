from django.shortcuts import render
from .forms import PizzaForm
# Create your views here.
def home(request):
    return render(request, "pizza/home.html")


def order(request):
    form= PizzaForm()
    return render(request, "pizza/order.html", {"pizza_form": form})
    # if request.method == "POST":
    #     # Process the order here
    #     return render(request, "pizza/order_success.html")
    # else:
    #     return render(request, "pizza/order_form.html")