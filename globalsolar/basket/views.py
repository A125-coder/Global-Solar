from django.shortcuts import render, redirect
from catalog.models import Catalog
from django.shortcuts import get_object_or_404
from django.urls import reverse

def index(request, product_id):
    product = get_object_or_404(Catalog, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, 'pages/basket.html', context)