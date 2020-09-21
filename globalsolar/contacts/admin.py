from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name',
                    'email', 'phone', 'date', 'address')
    list_links = ("name", "email", "phone")
    list_editable = ("name", "email", "phone")
    list_per_page = 30


admin.site.register(Contact, ContactAdmin)
