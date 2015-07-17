import django_filters
from .models import Offer

class OfferFilter(django_filters.FilterSet):
    min_floor_space = django_filters.NumberFilter(lookup_type='gte')
    max_floor_space = django_filters.NumberFilter(lookup_type='lte')
    min_price = django_filters.NumberFilter(lookup_type='gte')
    max_price = django_filters.NumberFilter(lookup_type='lte')
    min_nb_rooms = django_filters.NumberFilter(lookup_type='gte')
    max_nb_rooms = django_filters.NumberFilter(lookup_type='lte')
    
    class Meta:
        model = Offer
        fields = [
            'transaction', 'category', 'province', 'city',
            'nb_rooms', 'min_floor_space', 'max_floor_space',
            'min_price', 'max_price', 'min_nb_rooms', 'max_nb_rooms'
            ]