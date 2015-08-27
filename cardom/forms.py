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
    from_email = forms.EmailField(required=True, label="Twój E-mail")
    subject = forms.CharField(required=True, widget=forms.TextInput, label="Temat", initial="Proszę o kontakt")
    message = forms.CharField(required=True, widget=forms.Textarea, label="Wiadomość", initial="Jestem zainteresowany ofertą")
    
        
    