from rest_framework import generics
from rest_framework.response import Response
from django.core.cache import cache
from .models import Product
from .serializers import ProductSerializer

CACHE_KEY = 'all_products'


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.select_related('category').all()

    def list(self, request, *args, **kwargs):
        cached_products = cache.get(CACHE_KEY)
        if cached_products is not None:
            return Response(cached_products)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        cache.set(CACHE_KEY, serializer.data, timeout=3600)  # Set to cache data for 1 hour
        return Response(serializer.data)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()
        cache.delete(CACHE_KEY)  # Cache Invalidation


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save()
        cache.delete(CACHE_KEY)  # Cache Invalidation


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete(CACHE_KEY)  # Cache Invalidation
