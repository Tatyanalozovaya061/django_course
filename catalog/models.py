from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория продукта')
    description = models.TextField(**NULLABLE, verbose_name='описание категории')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание продукта')
    image = models.ImageField(upload_to='product_image/', **NULLABLE, verbose_name='изображение продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория продукта')
    price = models.FloatField(verbose_name='стоимость за единицу')
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликован')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='продавец')

    def __str__(self):
        return f"{self.name} по цене: {self.price}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            ('set_is_published', 'разрешено менять публикацию товаров'),
            ('set_description', 'разрешено менять описание товаров'),
            ('set_category', 'разрешено менять категорию товаров'),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='активность версии')

    def __str__(self):
        return f'{self.product} - {self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
