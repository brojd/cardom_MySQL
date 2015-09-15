# -*- coding: utf-8 -*-

from django import forms
from models import Offers

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

class PublishForm(forms.Form):
    from_email = forms.EmailField(required=True, label="Twój e-mail")
    phone_nb = forms.CharField(required=True, label="Numer telefonu")
    category = forms.CharField(required=True, label="Typ obiektu")
    location = forms.CharField(required=True, label="Lokalizacja")
    price = forms.CharField(required=True, label="Cena")
    description = forms.CharField(required=False, widget=forms.Textarea, label="Dodatkowy opis")

    
        
    