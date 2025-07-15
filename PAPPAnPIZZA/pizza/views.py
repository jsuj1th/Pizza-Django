from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pizza/home.html")


def order(request):
    return render(request, "pizza/order.html")
    # if request.method == "POST":
    #     # Process the order here
    #     return render(request, "pizza/order_success.html")
    # else:
    #     return render(request, "pizza/order_form.html")