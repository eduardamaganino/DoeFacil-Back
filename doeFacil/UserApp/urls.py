from django.urls import path
from . import views

urlpatterns = [
    path('users', views.userApi),
    path('users/<str:id>', views.userApi),
    path('itens', views.itemApi),
    path('itens/<str:id>', views.itemApi),
    path('doacoes', views.doacaoApi),
    path('doacoes/<str:id>', views.doacaoApi),
]