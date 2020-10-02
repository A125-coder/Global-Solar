from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Catalog
from django.urls import reverse
from .forms import CartAddProductForm
from .basket import Basket

# def index(request, product_id):
#     product = get_object_or_404(Catalog, pk=product_id)
#     context = {
#         "product": product,
#     }
#     return render(request, 'pages/basket.html', context)

@require_POST
def cart_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Catalog, pk=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('basket:cart_detail')

def cart_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Catalog, id=product_id)
    basket.remove(product)
    return redirect('basket:cart_detail')

def cart_detail(request):
    basket = Basket(request)
    for item in basket:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'],'update': True})
    return render(request, 'pages/basket.html', {"basket": basket})