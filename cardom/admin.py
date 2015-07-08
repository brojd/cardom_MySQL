from django.contrib import admin
from .models import Category, Offer, OfferImage
# Register your models here.
admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(OfferImage)

class OfferImageInline(admin.TabularInline):
    model = OfferImage
    fk_name = 'offer'
    extra = 5

class OfferAdmin(admin.ModelAdmin):
    inlines = [ OfferImageInline, ]
    list_display = ('id', 'category', 'city', 'district', 'floor_space', 'price')

admin.site.unregister(Offer)
admin.site.register(Offer, OfferAdmin)