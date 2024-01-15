from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        vegetables = Category(name='Vegetables').save()
        fruits = Category(name='Fruits').save()
        grocery = Category(name='Grocery').save()

        product_list = [
            {'name': 'помидоры', 'price': 250, 'category': vegetables},
            {'name': 'огурцы соленые', 'price': 200, 'category': vegetables},
            {'name': 'яблоки', 'price': 150, 'category': fruits},
            {'name': 'груши', 'price': 200, 'category': fruits},
            {'name': 'изюм', 'price': 300, 'category': grocery},
            {'name': 'макадамия', 'price': 800, 'category': grocery}
        ]
        products = []
        for product_item in product_list:
            products.append(Product(**product_item))
        Product.objects.bulk_create(products)
