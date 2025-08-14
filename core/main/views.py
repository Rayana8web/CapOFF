
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db models import Q
from .models import Product, Category, Brand, Banner
from .serializers import ProductListSerializer, CategoryListSerializer, BrandListSerializer, BannerListSerializer


class IndexView(APIView):
    def get(self, request):
        index_banners = Banner.objects.filter(Q(location='index_head') | Q(location='index_middle'), is_active=True)
        popular_brands = Brand.objects.all()[:4]
        best_seller_products = Product.objects.all()[:4]
        discounted_products =Product.objects.filter(new_price_isnull=False)[:4]
        products = Product.objects.filter(is_active=True)
        categories = Category.objects.all()
        brands = Brand.objects.all()

        data = {

        'products': ProductListSerializer(products, many=True).data,
        'categories': CategoryListSerializer(categories, many=True).data,
        'brands': BrandListSerializer(brands, many=True).data,
        'index_banners_serializer' : BannerListSerializer(index_banners, many=True).data,
        'popular_brands_serializer' : BrandListSerializer(popular_brands, many=True).data,
        'best_seller_products_serializer' : ProductListSerializer(best_seller_products, many=True).data,
        'discounted_products_serializer' :  ProductListSerializer(discounted_products, many=True).data,

    }

        return Response(data)

class CatalogView(APIView):
    def get(self, request):

        index_banners = Banner.objects.filter(
            Q(location='index_head') | Q(location='index_middle'),
            is_active=True
        )


        products = Product.objects.filter(is_active=True)


        data = {
            'products': ProductListSerializer(products, many=True).data,
            'index_banners': BannerListSerializer(index_banners, many=True).data,
        }

        return Response(data)