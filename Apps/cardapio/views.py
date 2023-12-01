from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

# models
from .models import Restaurant, CategoryMenu, Product
from .forms import RestaurantForm, CategoryMenuForm, ProductForm

import qrcode


def index(request):
    print(request.build_absolute_uri())
    template_name = 'index.html'
    try:
        restaurants = Restaurant.objects.all()
    except:
        return HttpResponse("Erro interno no servidor")
    return render(request, template_name, {'restaurants': restaurants})


def create_restaurant(request):
    template_name = 'create_restaurant.html'
    
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                restaurant = Restaurant(
                    name=form.cleaned_data['name'],
                    logo=form.cleaned_data['logo'],
                    contact=form.cleaned_data['contact']
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
    return render(request, template_name, {'restaurant': restaurant, 'categories': categories,})


def detail_restaurant_category(request, slug):
    template_name = 'detail_restaurant_category.html'

    restaurant = get_object_or_404(Restaurant, slug=slug)
    categories = CategoryMenu.objects.filter(restaurant=restaurant)

    category_selected = request.GET.get('category')
    if category_selected:
        products = Product.objects.filter(category__title__icontains=category_selected)

        return render(request, template_name, {'restaurant': restaurant, 'categories': categories, 'products': products})

    return render(request, template_name, {'restaurant': restaurant, 'categories': categories,})


def admin_area(request, slug):
    template_name = 'admin_area.html'
    restaurant = get_object_or_404(Restaurant, slug=slug)
    absolute_url = request.build_absolute_uri()

    qr = qrcode.make(absolute_url)
    print(qr)

    
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
                    return redirect(reverse_lazy('detail_restaurant', args=[slug]))
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
                    return redirect(reverse_lazy('detail_restaurant', args=[slug]))
    else:
        form_category = CategoryMenuForm()
        form_product = ProductForm()

    return render(request, template_name, {'restaurant': restaurant, 'form_category': form_category, 'form_product': form_product, 'qr': qr})
