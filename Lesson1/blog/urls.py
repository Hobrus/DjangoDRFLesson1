from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ShopViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns = [
    path('', include(router.urls))
]
