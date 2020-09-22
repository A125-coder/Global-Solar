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
    path('ses/', views.ses, name="ses"),
    path('faq/', views.faq, name="faq"),
]
