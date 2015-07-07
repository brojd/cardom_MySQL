from django.db import models

# Create your models here.
class Category(models.Model):
    
    NAME_CHOICES = (
        ('D', 'DOMY'),
        ('M', 'MIESZKANIA'),
        ('L', 'LOKALE'),
        ('DZ', 'DZIALKI'),
        ('O', 'OBIEKTY'),
    )
    
    name = models.CharField(max_length=128, choices=NAME_CHOICES, verbose_name='Nazwa Kategorii', default='M')
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.name



class Offer(models.Model):
    category = models.ForeignKey(Category, verbose_name='Kategoria')
    city = models.CharField(max_length=128, verbose_name='Miasto')
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
    province = models.CharField(max_length=3, choices=PROVINCE_CHOICES, default='OPO', verbose_name='Wojewodztwo')
    district = models.CharField(max_length=128, verbose_name='Dzielnica')
    nb_rooms = models.IntegerField(verbose_name='Liczba pokoi')
    floor_space = models.IntegerField(verbose_name='Powierzchnia [m2]')
    price = models.IntegerField(verbose_name='cena [zl]')
    
    def __unicode__(self):
        return "Oferta nr %s" % (self.id)