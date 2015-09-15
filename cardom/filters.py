#-*- coding: utf-8 -*-

import django_filters
from .models import Offers

class OfferFilter(django_filters.FilterSet):
    min_floor_space = django_filters.NumberFilter(lookup_type='gte')
    max_floor_space = django_filters.NumberFilter(lookup_type='lte')
    min_price = django_filters.NumberFilter(lookup_type='gte')
    max_price = django_filters.NumberFilter(lookup_type='lte')
    min_nb_rooms = django_filters.NumberFilter(lookup_type='gte')
    max_nb_rooms = django_filters.NumberFilter(lookup_type='lte')
    
    
    class Meta:
        model = Offers
        fields = [
            'object', 'province', 'district', 'location', 'rent',
            'rooms_no', 'min_floor_space', 'max_floor_space',
            'min_price', 'max_price'
            ]