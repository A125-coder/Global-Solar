from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="portfolio"),
    path('<int:work_id>', views.work, name="work"),
]
