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