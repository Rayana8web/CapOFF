from django.urls import path
from . import views
from .views import (CatalogView, BasketView, AddToBasketView, RemoveFromBasketView,
                    ClearBasketView, FavoriteListView, ToggleFavoriteView, ProductListView, CreateOrderView)


urlpatterns = [
    path('index/', views.IndexView.as_view()),
    path('catalog/', CatalogView.as_view(), ),
    path("basket/", BasketView.as_view(), ),
    path("basket/add/", AddToBasketView.as_view(), ),
    path("basket/remove/", RemoveFromBasketView.as_view(), ),
    path("basket/clear/", ClearBasketView.as_view(),),
    path("favorites/", FavoriteListView.as_view(), ),
    path("favorites/<int:product_id>/toggle/", ToggleFavoriteView.as_view(),),
    path("products/", ProductListView.as_view(), ),
    path("orders/create/", CreateOrderView.as_view(), ),
]
