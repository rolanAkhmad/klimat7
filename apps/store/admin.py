from django.contrib import admin
from .models import Category, Product, ProductGalery

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ProductGalery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    list_display = ('id', 'title', 'slug', 'category', 'manufacturer', 'price', 'in_stock')
    list_display_links = ('title', 'category',)
    list_filter = ('category', 'manufacturer','in_stock')
    # search_fields = ('title', 'category__name',)

    fieldsets = (
        ('Основное', {
            'fields': ('title','slug','category','price','in_stock','manufacturer')
        }),
        ('Описание', {
            'fields': ('description', 'detail_description')
        }),
    )
    
admin.site.register(Category)
