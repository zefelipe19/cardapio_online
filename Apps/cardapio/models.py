from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image


class BaseModelTamplate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updatad_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        abstract = True


class Restaurant(BaseModelTamplate):
    name = models.CharField(max_length=255, verbose_name='Nome')
    logo = models.ImageField(upload_to='restaurants/', verbose_name='Logo')
    contact = models.CharField(max_length=11, verbose_name='Telefone')
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'

    def __str__(self):
        return f'{self.name}'
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}')
        super().save(*args, **kwargs)
        if self.logo:
            SIZE = (700, 700)
            logo = Image.open(self.logo.path)
            logo.thumbnail(SIZE, Image.LANCZOS)
            logo.save(self.logo.path)
        return


class CategoryMenu(BaseModelTamplate):
    TYPE_CHOICES = (
        ('AL', 'Alimento'),
        ('BE', 'Bebida'),
    )

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='Cardapio')
    title = models.CharField(max_length=255, verbose_name='Título')
    type_category = models.CharField(max_length=2, verbose_name='Tipo de categoria', choices=TYPE_CHOICES)

    
    class Meta:
        verbose_name = 'Categoria Restaurante'
        verbose_name_plural = 'Categorias Restaurante'

    def __str__(self):
        return f'{self.title}'
    

    def get_products(self):
        products = Product.objects.filter(category=self.id).all()
        return products
    

class Product(BaseModelTamplate):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='Restaurante')
    category = models.ForeignKey(CategoryMenu, on_delete=models.CASCADE, verbose_name='Categoria')
    is_active = models.BooleanField(default=True, verbose_name='Em estoque')

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='restaurant/products/', verbose_name='Foto', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=1, verbose_name='Preço')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.name} - {self.category} - {self.restaurant}'
