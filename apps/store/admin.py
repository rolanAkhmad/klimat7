from django.contrib import admin
from .models import Category, Product, ProductGalery

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ProductGalery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    list_display = ('id','title', 'category','price',)
    list_display_links = ('title', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'category__name',)


admin.site.register(Category)
