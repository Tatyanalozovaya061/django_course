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
    # date_create = models.DateField(**NULLABLE, verbose_name='date_create')
    # change_data = models.DateField(**NULLABLE, verbose_name='change_data')

    def __str__(self):
        return f"{self.name} по цене: {self.price}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
