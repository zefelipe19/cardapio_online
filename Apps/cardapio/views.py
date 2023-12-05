from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

# models
from .models import Restaurant, CategoryMenu, Product
from .forms import RestaurantForm, CategoryMenuForm, ProductForm
from .utils import gerate_qr_code

from django.db import connection

def conections_counter():
    print(f'Numero de consultas no banco: {len(connection.queries)}')


def index(request):
    template_name = 'index.html'
    try:
        restaurants = Restaurant.objects.all()
    except:
        return HttpResponse("Erro interno no servidor")
    conections_counter()
    return render(request, template_name, {'restaurants': restaurants})


def create_restaurant(request):
    template_name = 'create_restaurant.html'
    
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                if request.user.is_authenticated:
                    user = request.user
                else:
                    user = None
                restaurant = Restaurant(
                    name=form.cleaned_data['name'],
                    logo=form.cleaned_data['logo'],
                    contact=form.cleaned_data['contact'],
                    user=user
                )
                if restaurant:
                    restaurant.save()
                    print(restaurant.slug)
                return redirect(reverse_lazy('admin_area', args=[restaurant.slug]))
            except:
                return HttpResponse("Erro interno no servidor")
        else:
            print(form.errors)
    else:
        form = RestaurantForm()
    return render(request, template_name, {'form': form})


def detail_restaurant(request, slug):
    template_name = 'detail_restaurant.html'
    restaurant = get_object_or_404(Restaurant, slug=slug)
    categories = CategoryMenu.objects.filter(restaurant=restaurant)

    conections_counter()

    return render(request, template_name, {'restaurant': restaurant, 'categories': categories,})


def detail_restaurant_category(request, slug):
    template_name = 'detail_restaurant_category.html'

    restaurant = get_object_or_404(Restaurant, slug=slug)
    categories = CategoryMenu.objects.filter(restaurant=restaurant).prefetch_related('products')

    category_selected = request.GET.get('category')
    if category_selected:
        products = Product.objects.filter(category__title__icontains=category_selected)
        conections_counter()

        return render(request, template_name, {'restaurant': restaurant, 'categories': categories, 'products': products})

    conections_counter()
    return render(request, template_name, {'restaurant': restaurant, 'categories': categories,})


def admin_area(request, slug):
    template_name = 'admin_area.html'
    restaurant = get_object_or_404(Restaurant, slug=slug)
    categories = CategoryMenu.objects.filter(restaurant=restaurant).prefetch_related('products')

    restaurant_qrCode = gerate_qr_code(request=request, slug=slug)
    
    if request.method == 'POST':
        form_category = CategoryMenuForm(request.POST)
        form_product = ProductForm(request.POST, request.FILES)

        if form_product or form_category:
            if form_category.is_valid():
                category = CategoryMenu(
                    restaurant=restaurant,
                    title=form_category.cleaned_data['title'],
                    type_category=form_category.cleaned_data['type_category'],
                )
                if category:
                    category.save()
                    return redirect(reverse_lazy('admin_area', args=[slug]))
            if form_product.is_valid():
                product = Product(
                    restaurant=restaurant,
                    category=form_product.cleaned_data['category'],
                    name=form_product.cleaned_data['name'],
                    image=form_product.cleaned_data['image'],
                    price=form_product.cleaned_data['price'],
                    description=form_product.cleaned_data['description'],
                )
                if product:
                    product.save()
                    return redirect(reverse_lazy('admin_area', args=[slug]))
    else:
        form_category = CategoryMenuForm()
        form_product = ProductForm()

    context = {
        'restaurant': restaurant,
        'categories': categories,
        'form_category': form_category, 
        'form_product': form_product, 
        'qr': restaurant_qrCode
    }
    conections_counter()
    return render(request, template_name, context)
