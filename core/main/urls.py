from django.urls import path
from . import views
from .views import CatalogView

urlpatterns = [
    path('index/', views.IndexView.as_view()),
    path('catalog/', CatalogView.as_view(), name='catalog'),

]
