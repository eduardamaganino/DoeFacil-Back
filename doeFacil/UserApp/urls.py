from django.urls import path
from . import views

urlpatterns = [
    path('users', views.userApi),
    path('users/<str:id>', views.userApi),
    path('users/<str:email>/<str:senha>', views.authUserApi),
    path('itens', views.itemApi),
    path('itens/<str:id>', views.itemApi),
    path('doacoes', views.doacaoApi),
    path('doacoes/<str:id>', views.doacaoApi),
]