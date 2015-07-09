from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Offer


# Create your views here.
def index(request):
    category_list = Category.objects.all
    latest_offers = Offer.objects.order_by('-pub_date')[:10]
    promoted_offers = Offer.objects.filter(promoted=True).order_by('-pub_date')[:10]
    
    context_dict = {'categories': category_list,
                    'latest_offers': latest_offers,
                    'promoted_offers': promoted_offers}
    
    return render(request, 'cardom/index.html', context_dict)

def flats(request):
    flat_offers = Offer.objects.filter(category__name='M').order_by('-pub_date')
    context_dict = {'flat_offers': flat_offers}
    return render(request, 'cardom/flats.html', context_dict)

def houses(request):
    house_offers = Offer.objects.filter(category__name='D').order_by('-pub_date')
    context_dict = {'house_offers': house_offers}
    return render(request, 'cardom/houses.html', context_dict)

def lots(request):
    lot_offers = Offer.objects.filter(category__name='DZ').order_by('-pub_date')
    context_dict = {'lot_offers': lot_offers}
    return render(request, 'cardom/lots.html', context_dict)