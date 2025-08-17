from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from orders.models import Order

@login_required
def payment_success(request, order_id):
    order = Order.objects.get(id=order_id, customer__user=request.user)
    order.status = "paid"
    order.save()
    return render(request, "payments/payment_success.html", {"order": order})

@login_required
def payment_failed(request, order_id):
    return render(request, "payments/payment_failed.html")


# Create your views here.
