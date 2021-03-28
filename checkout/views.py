from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ia4WcB87QiGthiQ6RsSj9JW0J7I6Yd8I7DrvlUXLDZiq9axTSW7IAjMtJUw1bodA3Njbc9Zpd89RXGhQc0OgQye00wLe6Ll0E',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)