from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category',
                                                     write_only=True)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category_id', 'category']

    def create(self, validated_data):
        category = validated_data.pop('category')
        return Product.objects.create(category=category, **validated_data)

    def update(self, instance, validated_data):
        category = validated_data.pop('category', None)
        if category:
            instance.category = category
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
