from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about_us/', views.about, name="about"),
    path('prices/', views.prices, name="prices"),
    path('contacts/', views.contacts, name="contacts"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('green_tarif/', views.green_tarif, name="green_tarif"),
    path('register/', views.register, name="register"),
    path('energy/', views.energy, name="energy"),
    path('one_work/', views.one_work, name="one_work"),
    path('our_works/', views.our_works, name="our_works"),
    path('catalog/', views.catalog, name="catalog"),
    path('product/', views.product, name="product"),
    path('ses/', views.ses, name="ses"),
    path('faq/', views.faq, name="faq"),
]
