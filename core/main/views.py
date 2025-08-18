from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Product, Category, Brand, Banner, Basket, BasketItem, Storage, Favorite
from .serializers import (ProductListSerializer, CategoryListSerializer, BrandListSerializer,
                          BannerListSerializer, BasketListSerializer, FavoriteSerializer)


class IndexView(APIView):
    def get(self, request):
        index_banners = Banner.objects.filter(Q(location='index_head') | Q(location='index_middle'), is_active=True)
        popular_brands = Brand.objects.all()[:4]
        best_seller_products = Product.objects.all()[:4]
        discounted_products = Product.objects.filter(new_price__isnull=False)[:4]

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




class BasketView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        basket, _ = Basket.objects.get_or_create(user=request.user)
        serializer = BasketListSerializer(basket)
        return Response(serializer.data)


class AddToBasketView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        storage_id = request.data.get("storage_id")
        quantity = int(request.data.get("quantity", 1))

        try:
            storage = Storage.objects.get(id=storage_id)
        except Storage.DoesNotExist:
            return Response({"error": "Такого размера/товара нет"}, status=status.HTTP_400_BAD_REQUEST)

        if storage.quantity < quantity:
            return Response({"error": "Недостаточно товара на складе"}, status=status.HTTP_400_BAD_REQUEST)

        basket, _ = Basket.objects.get_or_create(user=request.user)
        item, created = BasketItem.objects.get_or_create(basket=basket, storage=storage)

        if not created:
            if storage.quantity < item.quantity + quantity:
                return Response({"error": "Недостаточно товара на складе"}, status=status.HTTP_400_BAD_REQUEST)
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

        serializer = BasketListSerializer(basket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemoveFromBasketView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        storage_id = request.data.get("storage_id")
        basket = Basket.objects.get(user=request.user)

        try:
            item = BasketItem.objects.get(basket=basket, storage_id=storage_id)
            item.delete()
            serializer = BasketListSerializer(basket)
            return Response(serializer.data)
        except BasketItem.DoesNotExist:
            return Response({"error": "Товара нет в корзине"}, status=status.HTTP_400_BAD_REQUEST)


class ClearBasketView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        basket = Basket.objects.get(user=request.user)
        basket.items.all().delete()
        serializer = BasketListSerializer(basket)
        return Response(serializer.data)


class ToggleFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            product=product
        )
        if not created:
            favorite.delete()
            return Response({"detail": "Удалено из избранного"}, status=status.HTTP_200_OK)

        return Response({"detail": "Добавлено в избранное"}, status=status.HTTP_201_CREATED)


class FavoriteListView(ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)