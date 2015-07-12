import django_filters
from .models import Offer

class OfferFilter(django_filters.FilterSet):
    floor_space = django_filters.RangeFilter(label='Powierzchnia [m2]')
    price = django_filters.RangeFilter(label='Cena')
    nb_rooms = django_filters.RangeFilter(label='Liczba pokoi')
    
    class Meta:
        model = Offer
        fields = ['transaction', 'category', 'province', 'city',  'nb_rooms', 'floor_space', 'price']