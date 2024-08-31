from django.core.management.base import BaseCommand
from api.models import Category


class Command(BaseCommand):
    help = 'Populates the Category model with predefined data'

    def handle(self, *args, **kwargs):
        categories = [
            {"name": "Electronics", "description": "Devices and gadgets"},
            {"name": "Home Appliances", "description": "Appliances for home use"},
            {"name": "Books", "description": "Various genres of books"},
        ]

        for category_data in categories:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={'description': category_data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created category: {category.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Category already exists: {category.name}'))

        self.stdout.write(self.style.SUCCESS('Finished populating categories'))
