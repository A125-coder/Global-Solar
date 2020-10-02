from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from basket.basket import Basket
from django.core.mail import send_mail


def order_create(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in basket:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            basket.clear()

            return render(request, 'pages/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'pages/create.html',
                  {'basket': basket, 'form': form})
