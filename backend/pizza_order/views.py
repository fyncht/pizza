from rest_framework import viewsets
from .models import PizzaOrder
from .serializers import PizzaOrderSerializer


class PizzaOrderViewSet(viewsets.ModelViewSet):
    queryset = PizzaOrder.objects.all().order_by('-created_at')
    serializer_class = PizzaOrderSerializer
