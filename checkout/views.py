from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KsW0LAVlLofNb8rVtvoq6PUa4dBQMiqg610n8jRSD45EcCLm9iB1vHQOrbVL8bM9QIyPQxOkUY3pHckcUsg6yk400uuQMbwwl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)