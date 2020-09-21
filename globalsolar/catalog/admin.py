from django.contrib import admin
from .models import Catalog


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'power', 'price', 'catalog_type', 'is_published')
    list_display_links = ('id', 'title', 'price')
    list_per_page = 30


admin.site.register(Catalog, CatalogAdmin)

