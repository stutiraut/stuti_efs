from django.contrib import admin

from .models import Customer


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_number', 'name', 'city', 'cell_phone')
    list_filter = ('cust_number', 'name', 'city')
    search_fields = ('cust_number', 'name')
    ordering = ['cust_number']



admin.site.register(Customer)
