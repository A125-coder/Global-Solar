from django.shortcuts import render, redirect
from .models import Catalog
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q

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
    SolarPanels = Catalog.objects.all().filter(Q(catalog_type='Solar Panels Monocrystalline') | Q(catalog_type='Solar Panels Polycrystalline'))
    print(SolarPanels)
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    print(page)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/catalogPage.html", context)

def monocrystalline(request):
    SolarPanels = Catalog.objects.all().filter(catalog_type='Solar Panels Monocrystalline')
    print(SolarPanels)
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    print(page)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/catalogMono.html", context)
    
def polycrystalline(request):
    SolarPanels = Catalog.objects.all().filter(catalog_type='Solar Panels Polycrystalline')
    print(SolarPanels)
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    print(page)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/catalogPoly.html", context)