from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    
    NAME_CHOICES = (
        ('D', 'DOMY'),
        ('M', 'MIESZKANIA'),
        ('L', 'LOKALE'),
        ('DZ', 'DZIALKI'),
        ('O', 'OBIEKTY'),
    )
    
    name = models.CharField(max_length=2, choices=NAME_CHOICES, verbose_name='Nazwa Kategorii', default='M')
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.get_name_display()



class Offer(models.Model):
    
    TRANSACTION_CHOICES = (
        ('S', 'SPRZEDAZ'),
        ('W', 'WYNAJEM'),
    )
    
    PROVINCE_CHOICES = (
        ('OPO', 'OPOLSKIE'),
        ('DLN', 'DOLNOSLASKIE'),
        ('SLK', 'SLASKIE'),
        ('PDK', 'PODKARPACKIE'),
        ('LBK', 'LUBUSKIE'),
        ('LBL', 'LUBELSKIE'),
        ('MLP', 'MALOPOLSKIE'),
        ('KJP', 'KUJAWSKO-POMORSKIE'),
        ('POM', 'POMORSKIE'),
        ('ZPM', 'ZACHODNIO-POMORSKIE'),
        ('LDZ', 'LODZKIE'),
        ('MZW', 'MAZOWIECKIE'),
        ('PDL', 'PODLASKIE'),
        ('WLK', 'WIELKOPOLSKIE'),
        ('SWK', 'SWIETOKRZYSKIE'),
        ('WRM', 'WARMINSKO-MAZURSKIE'),
    )
    
    
    category = models.ForeignKey(Category, verbose_name='Rodzaj obiektu')
    city = models.CharField(max_length=128, verbose_name='Miasto')
    province = models.CharField(max_length=3, choices=PROVINCE_CHOICES, default='OPO', verbose_name='Wojewodztwo')
    district = models.CharField(max_length=128, verbose_name='Dzielnica')
    nb_rooms = models.IntegerField(verbose_name='Liczba pokoi')
    floor_space = models.IntegerField(verbose_name='Powierzchnia [m2]')
    price = models.IntegerField(verbose_name='cena [zl]')
    transaction = models.CharField(max_length=1, choices=TRANSACTION_CHOICES, verbose_name='Typ transakcji', default='S')
    balcony = models.BooleanField(verbose_name='Balkon', default=True)
    promoted = models.BooleanField(verbose_name='Promowana', default=False)
    pub_date = models.DateTimeField(verbose_name='Data publikacji', default=timezone.now())

    def __unicode__(self):
        return "Oferta nr %s" % (self.id)


class OfferImage(models.Model):
    
    offer = models.ForeignKey(Offer, related_name='images')
    images = models.ImageField(verbose_name="zdjecia", blank=True, null=True)
    main_image = models.BooleanField(verbose_name='zdjecie glowne', default=False)
    
    