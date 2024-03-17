from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from shop.models import Contact, Product, Supplier, Seller


@admin.register(Contact)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['email', 'country', 'city', 'street', 'house']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'product', 'level']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'product', 'supplier_link', 'debt', 'created_at']
    list_filter = ['contact__city']
    list_display_links = ['supplier_link']
    actions = ('clear_debt',)

    @admin.action(description='Очистить задолжность')
    def clear_debt(self, _, queryset):
        queryset.update(debt=0.00)

    def supplier_link(self, obj):
        link = reverse("admin:shop_supplier_change", args=[obj.supplier.id])
        return format_html('<a href="{}">{}</a>', link, obj.supplier.name)

    supplier_link.short_description = 'Поставщик'
