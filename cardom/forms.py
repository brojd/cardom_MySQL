# -*- coding: utf-8 -*-

from django import forms
from models import Offer

class OfferSort(forms.Form):
    SORT_CHOICES = (
        ('PDM', 'DATA PUBLIKACJI MALEJĄCO'),
        ('PDR', 'DATA PUBLIKACJI ROSNĄCO')
    )
    
    sort_offer = forms.ChoiceField(choices=SORT_CHOICES)
        
    