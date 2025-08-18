from django.urls import path
from . import views
from .views import CatalogView, BasketView, AddToBasketView, RemoveFromBasketView, ClearBasketView


urlpatterns = [
    path('index/', views.IndexView.as_view()),
    path('catalog/', CatalogView.as_view(), ),
    path("basket/", BasketView.as_view(), ),
    path("basket/add/", AddToBasketView.as_view(), ),
    path("basket/remove/", RemoveFromBasketView.as_view(), ),
    path("basket/clear/", ClearBasketView.as_view(),),
]
