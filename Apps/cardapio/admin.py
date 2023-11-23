from django.contrib import admin
from .models import Restaurant, CategoryMenu, Product

# Register your models here.

class CategoryAdminInline(admin.TabularInline):
    model = CategoryMenu
    readonly_fields = ('id',)
    extra = 1


class ProductAdminInline(admin.TabularInline):
    model = Product
    readonly_fields = ('id',)
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    inlines = (CategoryAdminInline, ProductAdminInline)


admin.site.register(Restaurant, RestaurantAdmin)
