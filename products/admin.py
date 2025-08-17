from django.contrib import admin
from .models import Product, Offer
from django.contrib import admin
#from .models import ContactMessage


admin.site.site_header = "My Shop Admin"          # Top-left title
admin.site.site_title = "My Shop Admin Portal"    # Browser tab title
admin.site.index_title = "Welcome to My Shop"     # Index page title



class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
