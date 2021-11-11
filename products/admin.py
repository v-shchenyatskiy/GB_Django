from django.contrib import admin

from products.models import ProductCategory, Product

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'category', 'image')
    readonly_fields = ('description',)
    ordering = ('name',)
    search_fields = ('name',)
