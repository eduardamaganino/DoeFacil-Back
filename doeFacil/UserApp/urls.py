from django.urls import include, path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('users', views.userApi),
    path('users/<str:id>', views.userApi),
    path('users/<str:email>/<str:senha>', views.authUserApi),
    path('itens', views.itemApi),
    path('itens/<str:id>', views.itemApi),
    path('doacoes', views.doacaoApi),
    path('doacoes/<str:id>', views.doacaoApi),
    
    path('auth/login/', obtain_jwt_token), #  remova esta linha
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
]