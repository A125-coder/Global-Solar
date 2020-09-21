from django.shortcuts import render, redirect
from .models import Catalog
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    catalog_prod = Catalog.objects.all()
    print(catalog_prod)
    
    paginator = Paginator(catalog_prod, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    context = {
        "catalog": page,
    }
    return render(request, "pages/catalog.html", context)


def product(request, product_id):
    product = get_object_or_404(Catalog, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "pages/product.html", context)

def SolarPanels(request):
    SolarPanels = Catalog.objects.all().filter(catalog_type="Solar Panels monocrystalline")
    print(SolarPanels)
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    print(page)
    context = {
        "product": page,
    }
    return render(request, "pages/catalogPage.html", context)

def monocrystalline(request):
    catalog_prod = Catalog.objects.order_by(
        '-list_date').filter(catalog_type='Solar Panels monocrystalline')
    paginator = Paginator(catalog_prod, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    context = {
        "product": page,
    }
    
    return render(request, "pages/catalog.html", context)
    
def polycrystalline(request):
    catalog_prod = Catalog.objects.order_by(
        '-list_date').filter(catalog_type='Solar Panels monocrystalline')
    paginator = Paginator(catalog_prod, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "product": page,
    }
    return render(request, "pages/catalog.html", context)