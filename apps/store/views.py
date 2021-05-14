from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import Product, Category

class ProductList(ListView):
    model = Product
    paginate_by = 9
    template_name = 'product_list.html'

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    object_list = category.products.all()

    paginator = Paginator(object_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'object_list': page_obj,
        'page_obj': page_obj,
        'paginator': paginator
    }
    
    return render(request, 'product_list_by_category.html', context)

def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(Q(title__icontains=query))

    context = {
        'query': query,
        'products': products,
    }

    return render(request, 'search.html', context)