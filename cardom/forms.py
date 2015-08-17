# -*- coding: utf-8 -*-

from django import forms
from models import Offer

class OfferSort(forms.Form):
    SORT_CHOICES = (
        ('PDM', 'DATA PUBLIKACJI MALEJĄCO'),
        ('PDR', 'DATA PUBLIKACJI ROSNĄCO'),
        ('PM', 'CENA MALEJĄCO'),
        ('PR', 'CENA ROSNĄCO'),
        ('FLM', 'POWIERZCHNIA MALEJĄCO'),
        ('FLR', 'POWIERZNIA ROSNĄCO')
    )
    
    sort_offer = forms.ChoiceField(choices=SORT_CHOICES, label="Sortuj według", required=False)
    

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    text = forms.TextInput(required=True)
        
    