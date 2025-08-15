from django.urls import path
from . import views
from .views import UserRegisterView

urlpatterns = [
    path('users/register/', views.UserRegisterView.as_view()),


]