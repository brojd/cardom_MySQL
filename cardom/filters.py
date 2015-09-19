#-*- coding: utf-8 -*-

import django_filters
from .models import Offers

class OfferFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    rooms_no = django_filters.RangeFilter()
    area = django_filters.RangeFilter()
    
    class Meta:
        model = Offers
        fields = [
            'object', 'province', 'district', 'location', 'rent', 'rooms_no',
            'price', 'area'
            ]