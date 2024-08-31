# Product-API

*Overview*
This project is a Django REST API that manages Product entities with associated Category. It provides endpoints for creating, retrieving, updating, and deleting products. The API optimizes query performance and caches results to reduce database load.

*Features*
CRUD Operations: Create, Read, Update, and Delete products.
Category Management: Manage product categories separately.
Caching: Cache product listings to reduce database hits.
Optimized Queries: Use Django’s select_related or prefetch_related to optimize queries.

*Prerequisites*

Python 3.11
Django 5.1
Django REST framework 3.15.2
django-redis 5.4.0
Redis 5.0.8
asgiref 3.8.1
sqlparse 0.5.1
tzdata 2024.1

Installation

*Clone the Repository*
git clone https://github.com/Austin-ik/Product-API.git
cd product-Api/enyata

Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies

Create or update requirements.txt with the following content:

Django==5.1
djangorestframework==3.15.2
django-redis==5.4.0
redis==5.0.8
asgiref==3.8.1
sqlparse==0.5.1
tzdata==2024.1

*Then install the dependencies:*

bash
Copy code
pip install -r requirements.txt

Cd to Question 2
*Apply Migrations*

python manage.py migrate

*Create Superuser*

python manage.py createsuperuser

*Run the Development Server*

python manage.py runserver

*API Endpoints*
1. Retrieve All Products
URL: /products/

Method: GET

Description: Retrieves a list of all products. Results are cached for efficiency.

Response:

json
Copy code
[
    {
        "id": 1,
        "name": "Smartphone",
        "description": "Latest model",
        "price": "699.99",
        "category": "Electronics"
    },
    ...
]

2. Create a Product
URL: /products/create/

Method: POST

Description: Creates a new product. The request must include category_id.

Request Body:

json
Copy code
{
    "name": "Smartwatch",
    "description": "Wearable tech",
    "price": "199.99",
    "category_id": 2
}
Response:

json
Copy code
{
    "id": 2,
    "name": "Smartwatch",
    "description": "Wearable tech",
    "price": "199.99",
    "category": "Wearables"
}

3. Update a Product
URL: /products/{id}/update

Method: PUT

Description: Updates the details of an existing product. The request must include category_id.

Request Body:

json
Copy code
{
    "name": "Smartphone Pro",
    "description": "Updated model",
    "price": "799.99",
    "category_id": 1
}
Response:

json
Copy code
{
    "id": 1,
    "name": "Smartphone Pro",
    "description": "Updated model",
    "price": "799.99",
    "category": "Electronics"
}

4. Delete a Product
URL: /products/{id}/delete
Method: DELETE
Description: Deletes a product by its ID.
Response: 204 No Content

*Management Commands*
Auto-populate Categories
You can use the management command to auto-populate categories:

python manage.py populate_categories

*Command Implementation*

Create a management command to populate categories:


# api/management/commands/populate_categories.py
from django.core.management.base import BaseCommand
from api.models import Category

class Command(BaseCommand):
    help = 'Populate categories'

    def handle(self, *args, **kwargs):
        categories = ['Electronics', 'Wearables', 'Home Appliances', 'etc']
        for category in categories:
            Category.objects.get_or_create(name=category)
        self.stdout.write(self.style.SUCCESS('Successfully populated categories'))
        
*Caching*
Caching is configured using Django Redis. Make sure Redis is installed and running. Update settings.py to include caching settings:

python
Copy code
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

*Troubleshooting*

"Method POST not allowed" Error: Check that the view is correctly configured to handle POST requests.
"Invalid data. Expected a dictionary, but got int": Ensure the category_id is provided correctly in the request.
