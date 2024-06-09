import django_filters
from .models import *
class orderFilters(django_filters.FilterSet):
    class Meta:
        model=Order
        fields=['book','status']