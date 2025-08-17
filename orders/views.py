from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.models import Product
from customers.models import Customer
from .models import Order


def add_to_cart(request, product_id ):
    cart = request.session.get('card', {})
    cart[product_id]= cart.get(product_id, 0)+1
    request.session['cart']= cart
    return redirect('cart_view')


def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = [(p, cart[str(p.id)]) for p in products]
    total = sum(p.price * qty for p, qty in cart_items)
    return render(request, "cart.html", {"cart_items": cart_items, "total": total})


# Create your views here.

# Show cart contents
def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = [(p, cart[str(p.id)]) for p in products]
    total = sum(p.price * qty for p, qty in cart_items)

    return render(request, "orders/cart.html", {
        "cart_items": cart_items,
        "total": total
    })


# Remove product from cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart_view')

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_view')  # nothing to checkout

    customer = Customer.objects.get(user=request.user)
    total_price = 0

    for pid, qty in cart.items():
        product = Product.objects.get(id=pid)
        total_price += product.price * qty

        Order.objects.create(
            customer=customer,
            product=product,
            quantity=qty,
            total_price=product.price * qty,
            status="pending"
        )

    request.session['cart'] = {}  # clear cart

    return render(request, "orders/checkout_success.html", {
        "total_price": total_price
    })

@login_required
def my_orders(request):
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(customer=customer).order_by('-id')  # latest first
    return render(request, "orders/my_orders.html", {"orders": orders})
