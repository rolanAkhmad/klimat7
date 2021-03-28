from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator

from apps.store.models import Product, Category

from .models import *

def frontpage(request):
    boiler_list = Product.objects.filter(category__slug="gas_boiler")
    new_product_list = Product.objects.order_by('-date_added')
    context = {
        'new_product_list':new_product_list,
        'boiler_list': boiler_list,
    }
    
    return render(request, 'index.html', context)

class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        # context['attributes'] = Attribute.objects.filter(product=product)
        context['products'] = Product.objects.filter(category__slug=product.category.slug)

        return context

def ProductListByCategory(request, slug):
    product_list = Product.objects.filter(category__slug=slug)
    return render(request, 'shop/product_list.html', context={'object_list':product_list})

