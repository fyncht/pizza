from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PizzaOrderViewSet

router = DefaultRouter()
router.register(r'orders', PizzaOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
