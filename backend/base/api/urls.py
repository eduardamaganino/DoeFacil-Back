from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.getRoutes),
    #path('notes/', views.getNotes),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', views.userApi),
    path('users/<str:id>', views.userApi),
    path('itens', views.itemApi),
    path('itens/<str:id>', views.itemApi),
    path('doacoes', views.doacaoApi),
    path('doacoes/<str:id>', views.doacaoApi),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)