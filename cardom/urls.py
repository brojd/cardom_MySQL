from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^flats/', views.flats, name='flats'),
    url(r'^houses/', views.houses, name='houses'),
    )