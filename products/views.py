from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """A view to show all products, including sorting and search queries."""

    products = Product.objects.all()
    query = None
    categories = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET and request.GET['sort'] != 'None':
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        else:
            products = products.annotate(lower_name=Lower('name'))
            products = products.order_by('lower_name')

        if 'category' in request.GET and request.GET['category'] != 'None':
            category = request.GET['category']
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET and request.GET['q'] != 'None':
            query = request.GET['q']
            if query is not None:
                queries = Q(
                    name__icontains=query) | Q(
                    description__icontains=query) | Q(
                    category__name__icontains=query)
                products = products.filter(queries)
    else:
        products = products.annotate(lower_name=Lower('name'))
        products = products.order_by('lower_name')

    current_sorting = f'{sort}_{direction}'

    paginator = Paginator(products, 8)
    page = request.GET.get('page')

    context = {
        'products': paginator.get_page(page),
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'category': category,
        'direction': direction,
        'sort': sort,
        'q': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_name, product_sku):
    """A view to show individual product details."""

    product = get_object_or_404(Product, name=product_name, sku=product_sku)
    products = Product.objects.all()
    products = products.order_by('?')
    products = products.filter(category__name__in=[product.category])
    products = products.exclude(pk=product.id)
    products = products[:3]

    context = {
        'product': product,
        'related_products': products,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """View for adding a product to the store."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail',
                                    args=[product.name, product.sku]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """View for editing a product in the store."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail',
                                    args=[product.name, product.sku]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """View for deleting a product from the store."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
