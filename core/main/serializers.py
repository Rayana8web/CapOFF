from rest_framework import serializers
from .models import (Category, Brand, Product,  ProductBrand,
                     Banner, Basket, BasketItem, Favorite, Order, OrderItems )








class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        exclude = ('is_active', )


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',  'title')

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'title', 'logo')


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    brands = serializers.SerializerMethodField()  # <-- убрали many=True

    class Meta:
        model = Product
        fields = ('id','brands', 'category',  'title', 'old_price', 'new_price', 'description', 'created_at', 'is_active')

    def get_brands(self, obj):
        pbs = obj.brands.all()
        return [
            {
                "id": b.id,
                "title": b.title,
                "logo": b.logo.url if b.logo else None
            }
            for b in pbs
        ]




class BasketItemListSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source="storage.product.title", read_only=True)
    size = serializers.CharField(source="storage.size.title", read_only=True)
    price = serializers.DecimalField(source="storage.product.new_price", read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = BasketItem
        fields = ["id", "storage", "product_title", "size", "price", "quantity", "created_at"]


class BasketListSerializer(serializers.ModelSerializer):
    items = BasketItemListSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ["id", "user", "items", "total_price"]
        read_only_fields = ["user", "total_price"]

    def get_total_price(self, obj):
        return obj.get_total_price()

class FavoriteSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source="product.title", read_only=True)
    product_price = serializers.DecimalField(source="product.new_price", max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Favorite
        fields = ["id", "product", "product_title", "product_price"]

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ["id", "storage", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "total_price", "status", "created_at", "items"]
        read_only_fields = ["user", "total_price", "status", "created_at", "items"]