from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

# models
from .models import Restaurant, CategoryMenu, Product
from .forms import RestaurantForm, CategoryMenuForm, ProductForm


def index(request):
    template_name = 'index.html'
    restaurants = Restaurant.objects.all()
    return render(request, template_name, {'restaurants': restaurants})


def create_restaurant(request):
    template_name = 'create_restaurant.html'
    
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('index'))
        else:
            print(form.errors)
    else:
        form = RestaurantForm()
    return render(request, template_name, {'form': form})


def detail_restaurant(request, slug):
    template_name = 'detail_restaurant.html'
    restaurant = get_object_or_404(Restaurant, slug=slug)
    categories = CategoryMenu.objects.filter(restaurant=restaurant)

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
                    return redirect(reverse_lazy('index'))
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
                    return redirect(reverse_lazy('index'))
    else:
        form_category = CategoryMenuForm()
        form_product = ProductForm()

    context = {
        'restaurant': restaurant,
        'categories': categories,
        'form_category': form_category,
        'form_product': form_product
    }
    return render(request, template_name, context)