from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [{
            "name": "овощи",
            "description": "корнеплоды, соленья"
        },
            {
                "name": "фрукты",
                "description": "ягоды, варенье"
            },
        ]

        categories = []
        for category_item in category_list:
            categories.append(Category(**category_item))

        Category.objects.bulk_create(categories)
