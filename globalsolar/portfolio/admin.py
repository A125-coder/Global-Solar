from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product_type',
                    'voltage', 'address', 'is_published', 'amount')
    list_display_links = ('id', 'address', 'title',)
    list_editable = ('is_published', 'product_type', 'voltage', 'amount',)
    list_per_page = 30
    search_fields = ('title', 'product_type', 'voltage')


admin.site.register(Portfolio, PortfolioAdmin)
