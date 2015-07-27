from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Offer, OfferImage
from .filters import OfferFilter
from .forms import OfferSort

# Create your views here.
def index(request):
    category_list = Category.objects.all
    latest_offers = Offer.objects.order_by('-pub_date')[:10]
    promoted_offers = Offer.objects.filter(promoted=True).order_by('-pub_date')[:10]
    f = OfferFilter(request.GET, queryset=Offer.objects.all())

    
    context_dict = {
        'categories': category_list,
        'latest_offers': latest_offers,
        'promoted_offers': promoted_offers,
        'filter': f,
                    }
    
    return render(request, 'cardom/index.html', context_dict)

def flats(request):
    flat_offers = Offer.objects.filter(category__name='M').order_by('-pub_date')
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-pub_date')
        elif sortby_choice=='PDR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('pub_date')
        elif sortby_choice=='PM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-price')
        elif sortby_choice=='PR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('price')
        elif sortby_choice=='FLM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-floor_space')
        elif sortby_choice=='FLR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('floor_space')
    context_dict = {
        'flat_offers': flat_offers,
        'filter': f,
        'form': form,
        }
    return render(request, 'cardom/flats.html', context_dict)

def houses(request):
    house_offers = Offer.objects.filter(category__name='D').order_by('-pub_date')
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-pub_date')
        elif sortby_choice=='PDR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('pub_date')
        elif sortby_choice=='PM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-price')
        elif sortby_choice=='PR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('price')
        elif sortby_choice=='FLM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-floor_space')
        elif sortby_choice=='FLR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('floor_space')
    context_dict = {
        'house_offers': house_offers,
        'filter': f,
        'form': form,
        }
    return render(request, 'cardom/houses.html', context_dict)

def lots(request):
    lot_offers = Offer.objects.filter(category__name='DZ').order_by('-pub_date')
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-pub_date')
        elif sortby_choice=='PDR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('pub_date')
        elif sortby_choice=='PM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-price')
        elif sortby_choice=='PR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('price')
        elif sortby_choice=='FLM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-floor_space')
        elif sortby_choice=='FLR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('floor_space')
    context_dict = {
        'lot_offers': lot_offers,
        'filter': f,
        'form': form,
        }
    return render(request, 'cardom/lots.html', context_dict)

def locals(request):
    local_offers = Offer.objects.filter(category__name='L').order_by('-pub_date')
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-pub_date')
        elif sortby_choice=='PDR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('pub_date')
        elif sortby_choice=='PM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-price')
        elif sortby_choice=='PR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('price')
        elif sortby_choice=='FLM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-floor_space')
        elif sortby_choice=='FLR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('floor_space')
    context_dict = {
        'local_offers': local_offers,
        'filter': f,
        'form': form,
        }
    return render(request, 'cardom/locals.html', context_dict)

def other_objects(request):
    other_object_offers = Offer.objects.filter(category__name='O').order_by('-pub_date')
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    if request.method=="GET":
        form = OfferSort(request.GET)
        sortby_choice = request.GET.get('sort_offer', '')
        if sortby_choice=='PDM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-pub_date')
        elif sortby_choice=='PDR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('pub_date')
        elif sortby_choice=='PM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-price')
        elif sortby_choice=='PR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('price')
        elif sortby_choice=='FLM':
            flat_offers = Offer.objects.filter(category__name='M').order_by('-floor_space')
        elif sortby_choice=='FLR':
            flat_offers = Offer.objects.filter(category__name='M').order_by('floor_space')
    context_dict = {
        'other_object_offers': other_object_offers,
        'filter': f,
        'form': form
        }
    return render(request, 'cardom/other_objects.html', context_dict)

def about(request):
    f = OfferFilter(request.GET, queryset=Offer.objects.all())    
    return render(request, 'cardom/about.html', {'filter': f})

def contact(request):
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    return render(request, 'cardom/contact.html', {'filter': f})

def career(request):
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    return render(request, 'cardom/career.html', {'filter': f})

def publish_offer(request):
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    return render(request, 'cardom/publish_offer.html', {'filter': f})

def credits(request):
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    return render(request, 'cardom/credits.html', {'filter': f})

def prices(request):
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    return render(request, 'cardom/prices.html', {'filter': f})

def offer_list(request):
    f = OfferFilter(request.GET, queryset=Offer.objects.all())
    return render(request, 'cardom/offer_list.html', {'filter': f})

def offer_details(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    return render(request, 'cardom/offer_details.html', {'offer': offer})


            