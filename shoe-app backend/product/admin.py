from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Store
from .models import Producer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_available', 'created_at', 'producer')
    list_display_links = ('id', 'name')
    list_filter = ('price',)
    list_editable = ('is_available',)
    search_fields = ('name', 'price')
    ordering = ('price',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Store)
admin.site.register(Producer)