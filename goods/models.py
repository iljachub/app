
from statistics import quantiles
from tabnanny import verbose
from django.db import models

class categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='Шлях URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='Шлях URL')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name= "Як виглядає товар" )
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name= "Ціна")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name= "Знижка у %")
    quantity= models.PositiveIntegerField(default=0, verbose_name= "Кількість")
    categories = models.ForeignKey(to=categories, on_delete=models.CASCADE, verbose_name= "Категорія")

    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
        
    def __str__(self):
        return f'{self.name} Кількість - {self.quantity}'
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.discount:
            return round (self.price - self.price*self.discount/100,  2)
        
        return self.price
    