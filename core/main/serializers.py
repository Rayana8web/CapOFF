from rest_framework import serializers
from .models import Category, Brand, Product,  ProductBrand, Banner

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
