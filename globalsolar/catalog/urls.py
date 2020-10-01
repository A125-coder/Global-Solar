from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="catalog"),
    path('<int:product_id>/', views.product, name="product"),

    path('ReadySolutions', views.ReadySolutions, name="ReadySolutions"),
    path('Autonomous', views.Autonomous, name="Autonomous"),
    path('OwnConsumption', views.OwnConsumption, name="OwnConsumption"),
    path('WaterHeating', views.WaterHeating, name="WaterHeating"),

    path('SolarInverters', views.SolarInverters, name="SolarInverters"),
    path('AutonomousInverters', views.AutonomousInverters,
         name="AutonomousInverters"),
    path('HybridInverters', views.HybridInverters, name="HybridInverters"),
    path('NetworkInverters', views.NetworkInverters, name="NetworkInverters"),

    path('SolarPanels', views.SolarPanels, name="SolarPanels"),
    path('monocrystalline', views.monocrystalline, name="monocrystalline"),
    path('polycrystalline', views.polycrystalline, name="polycrystalline"),
]
