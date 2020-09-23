from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="catalog"),
    path('<int:product_id>/', views.product, name="product"),
    path('SolarPanels/', views.SolarPanels, name="SolarPanels"),
    path('monocrystalline', views.monocrystalline, name="monocrystalline"),
    path('polycrystalline', views.polycrystalline, name="polycrystalline"),
]
