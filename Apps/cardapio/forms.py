from django import forms
from .models import Restaurant, CategoryMenu, Product


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'logo', 'contact', )


class CategoryMenuForm(forms.ModelForm):
    class Meta:
        model = CategoryMenu
        fields = ('title', 'type_category')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'image', 'price', 'description')
        