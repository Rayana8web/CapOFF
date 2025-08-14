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
    brands = serializers.SerializerMethodField(many=True)

    class Meta:
        model = Product
        fields = ('id','brands', 'category',  'title', 'old_price', 'new_price', 'description', 'created_at', 'is_active')

    def get_brand(self, obj):
        pb = ProductBrand.objects.filter(product=obj).select_related("brand").first()
        if pb:

            return {
                "id": pb.brand.id,
                "title": pb.brand.title,
                "logo": pb.brand.logo.url if pb.brand.logo else None
            }
        return None


