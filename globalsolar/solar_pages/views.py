from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        volts = request.POST["volts"]

        send_mail(
            "Прорахунок вартості пропозиції",
            "Я хочу станцію на:" + ", " + volts +
            ", " + name + ", " + email + " " + phone,
            'master@gmail.com',
            # Теж ваша електронка - куди буде лист відправлятися
            ['sup2a1nn@gmail.com'],
            fail_silently=False
        )
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about_us.html')


def prices(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        volts = request.POST["volts"]

        send_mail(
            "Прорахунок вартості пропозиції",
            "Я хочу станцію на:" + ", " + volts +
            ", " + name + ", " + email + " " + phone,
            'master@gmail.com',
            # Теж ваша електронка - куди буде лист відправлятися
            ['sup2a1nn@gmail.com'],
            fail_silently=False
        )
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


def catalog(request):
    return render(request, 'pages/catalog.html')


def product(request):
    return render(request, 'pages/product.html')


def ses(request):
    return render(request, 'pages/ses.html')


def faq(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        question = request.POST["question"]

        send_mail(
            "Моє запитання",
            question + ", " + name + ", " + email,
            'master@gmail.com',
            # Теж ваша електронка - куди буде лист відправлятися
            ['sup2a1nn@gmail.com'],
            fail_silently=False
        )
    return render(request, 'pages/faq.html')
