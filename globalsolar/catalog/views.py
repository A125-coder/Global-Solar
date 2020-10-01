from django.shortcuts import render, redirect
from .models import Catalog
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q
from . import views
from basket.forms import CartAddProductForm

def index(request):
    catalog_prod = Catalog.objects.all()
    paginator = Paginator(catalog_prod, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    context = {
        "catalog": page,
    }
    return render(request, "pages/catalog.html", context)




def product(request, product_id):
    product = get_object_or_404(Catalog, pk=product_id)
    cart_product_form = CartAddProductForm()
    context = {
        "product": product,
        'cart_product_form':cart_product_form,
    }
    return render(request, "pages/product.html", context)

def SolarPanels(request):
    SolarPanels = Catalog.objects.all().filter(Q(catalog_type='monocrystalline') | Q(catalog_type='polycrystalline') | Q(catalog_type='SolarPanels'))
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/catalogPage.html", context)

def monocrystalline(request):
    SolarPanels = Catalog.objects.all().filter(Q(catalog_type='monocrystalline') | Q(catalog_type='SolarPanels'))
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/catalogMono.html", context)
    
def polycrystalline(request):
    SolarPanels = Catalog.objects.all().filter(Q(catalog_type='polycrystalline') | Q(catalog_type='SolarPanels'))
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/catalogPoly.html", context)

def ReadySolutions(request):
    SolarPanels = Catalog.objects.all().filter(Q(catalog_type='Autonomous') | Q(catalog_type='OwnConsumption') | Q(catalog_type='WaterHeating'))
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/ReadySolutions.html", context)

def Autonomous(request):
    SolarPanels = Catalog.objects.all().filter(catalog_type='Autonomous')
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/Autonomous.html", context)

def OwnConsumption(request):
    SolarPanels = Catalog.objects.all().filter(catalog_type='OwnConsumption')
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/OwnConsumption.html", context)

def WaterHeating(request):
    SolarPanels = Catalog.objects.all().filter(catalog_type='WaterHeating')
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/WaterHeating.html", context)

def SolarInverters(request):
    SolarPanels = Catalog.objects.all().filter(Q(catalog_type='AutonomousInverters') | Q(catalog_type='HybridInverters') | Q(catalog_type='NetworkInverters'))
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/SolarInverters.html", context)

def AutonomousInverters(request):
    SolarPanels = Catalog.objects.all().filter(catalog_type='AutonomousInverters')
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/AutonomousInverters.html", context)

def HybridInverters(request):
    SolarPanels = Catalog.objects.all().filter(Q(catalog_type='AutonomousInverters') | Q(catalog_type='HybridInverters'))
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/HybridInverters.html", context)

def NetworkInverters(request):
    SolarPanels = Catalog.objects.all().filter(catalog_type='NetworkInverters')
    
    paginator = Paginator(SolarPanels, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        "SolarPanels": page,
    }
    return render(request, "pages/catalog/NetworkInverters.html", context)



