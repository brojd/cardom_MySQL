# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

#-*- coding: utf-16 -*-

from __future__ import unicode_literals

from django.db import models


class Agents(models.Model):
    id_other = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)
    cell = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    departments_id = models.IntegerField()
    jabber_login = models.CharField(max_length=20, blank=True, null=True)
    licence_no = models.CharField(max_length=50, blank=True, null=True)
    responsible_name = models.CharField(max_length=50, blank=True, null=True)
    responsible_licence_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agents'


class CardomAdmin(models.Model):
    login = models.CharField(max_length=50)
    pass_field = models.CharField(db_column='pass', max_length=50)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'cardom_admin'


class CardomAds(models.Model):
    matka = models.IntegerField()
    file = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    date = models.DateTimeField()
    publikuj = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cardom_ads'


class CardomAudio(models.Model):
    matka = models.IntegerField()
    name = models.TextField()
    date = models.DateTimeField()
    file = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cardom_audio'


class CardomContent(models.Model):
    nr = models.IntegerField()
    name = models.TextField()
    lead = models.TextField()
    content = models.TextField()
    kind = models.CharField(max_length=4)
    date = models.DateTimeField()
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cardom_content'


class CardomGallery(models.Model):
    matka = models.IntegerField()
    name = models.TextField()
    date = models.DateTimeField()
    file = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cardom_gallery'


class CardomInfo(models.Model):
    content = models.TextField()
    publikuj = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cardom_info'


class CardomInfo2(models.Model):
    matka = models.IntegerField()
    name = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()
    publikuj = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cardom_info2'


class CardomMenu(models.Model):
    id_menu = models.IntegerField()
    name = models.TextField()
    url = models.CharField(max_length=200)
    date = models.DateTimeField()
    main = models.CharField(max_length=1, blank=True, null=True)
    kind = models.CharField(max_length=5)
    kolejnosc = models.IntegerField()
    autor = models.CharField(max_length=60)
    publikuj = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cardom_menu'


class CardomNews(models.Model):
    matka = models.IntegerField()
    name = models.TextField()
    lead = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()
    file = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cardom_news'


class CardomRss(models.Model):
    title = models.TextField()
    link = models.TextField()

    class Meta:
        managed = False
        db_table = 'cardom_rss'


class CardomWideo(models.Model):
    matka = models.IntegerField()
    name = models.TextField()
    date = models.DateTimeField()
    file = models.CharField(max_length=50)
    kod = models.TextField()

    class Meta:
        managed = False
        db_table = 'cardom_wideo'


class Departments(models.Model):
    id_other = models.IntegerField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=6, blank=True, null=True)
    nip = models.CharField(max_length=20, blank=True, null=True)
    province = models.CharField(max_length=50)
    www = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    fax = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Errors(models.Model):
    date = models.DateTimeField()
    method = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'errors'


class Investments(models.Model):
    id_other = models.IntegerField()
    no = models.IntegerField()
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    map_marker = models.CharField(max_length=500, blank=True, null=True)
    garage = models.IntegerField()
    pool = models.IntegerField(blank=True, null=True)
    terrace = models.IntegerField(blank=True, null=True)
    air_conditioning = models.IntegerField(blank=True, null=True)
    house_project = models.IntegerField(blank=True, null=True)
    special = models.IntegerField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    total_area = models.DecimalField(max_digits=18, decimal_places=2)
    gross_volume = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    area_from = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    area_to = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    price_from = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    price_to = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pricem2_from = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pricem2_to = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    floor_from = models.IntegerField(blank=True, null=True)
    floor_to = models.IntegerField(blank=True, null=True)
    rooms_no_from = models.IntegerField(blank=True, null=True)
    rooms_no_to = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    quarter = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    departments_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'investments'


class InvestmentsBuildings(models.Model):
    id_other = models.IntegerField()
    investments_id = models.IntegerField()
    symbol = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    due_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    floors_no = models.IntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investments_buildings'


class Offers(models.Model):
    id_other = models.IntegerField()
    object = models.CharField(max_length=20)
    rent = models.IntegerField()
    symbol = models.CharField(max_length=20)
    original = models.IntegerField()
    province = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    quarter = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    floor = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    price_square = models.DecimalField(max_digits=18, decimal_places=2)
    rooms_no = models.IntegerField()
    area = models.DecimalField(max_digits=18, decimal_places=2)
    latitude = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    building_technology = models.CharField(max_length=200, blank=True, null=True)
    construction_material = models.CharField(max_length=200, blank=True, null=True)
    construction_status = models.CharField(max_length=200, blank=True, null=True)
    building_type = models.CharField(max_length=200, blank=True, null=True)
    agents_id = models.IntegerField()
    investments_buildings_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateField()
    modification_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'offers'


class OffersPhotos(models.Model):
    id_other = models.IntegerField()
    offers_id = models.IntegerField(blank=True, null=True)
    investments_id = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    order = models.IntegerField()
    type = models.CharField(max_length=20)
    intro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers_photos'


class OffersProperties(models.Model):
    offers_id = models.IntegerField()
    properties_id = models.IntegerField()
    value = models.TextField()
    set = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'offers_properties'


class OffersRooms(models.Model):
    offers_id = models.IntegerField()
    kind = models.CharField(max_length=25)
    order = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)
    level = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    height = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    kitchen_type = models.CharField(max_length=100, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    glaze = models.CharField(max_length=100, blank=True, null=True)
    window_view = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    floors_state = models.CharField(max_length=100, blank=True, null=True)
    room_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers_rooms'


class OffersRoomsSets(models.Model):
    offers_rooms_id = models.IntegerField()
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'offers_rooms_sets'


class Properties(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'properties'


class Settings(models.Model):
    key_name = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'settings'
