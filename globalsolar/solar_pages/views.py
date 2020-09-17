from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about_us.html')


def prices(request):
    return render(request, 'pages/prices.html')


def contacts(request):
    return render(request, 'pages/contacts.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')


def green_tarif(request):
    return render(request, 'pages/green_tarif.html')


def register(request):
    return render(request, 'pages/register.html')


def energy(request):
    return render(request, 'pages/energy.html')


def our_works(request):
    return render(request, 'pages/our_works.html')


def one_work(request):
    return render(request, 'pages/one_work.html')


def catalog(request):
    return render(request, 'pages/catalog.html')


def product(request):
    return render(request, 'pages/product.html')


def ses(request):
    return render(request, 'pages/ses.html')


def  faq(request):
    return render(request, 'pages/faq.html')
