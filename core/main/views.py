from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Brand
from .serializers import ProductListSerializer, CategoryListSerializer, BrandListSerializer


@api_view(['GET'])

def main_page(request):
    user = request.user
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    brands = Brand.objects.all()

    data = {

        'products': ProductListSerializer(products, many=True).data,
        'categories': CategoryListSerializer(categories, many=True).data,
        'brands': BrandListSerializer(brands, many=True).data,
    }

    return Response(data)