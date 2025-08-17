from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'country','joined_at')
    list_display= ('user__username','phone', 'city', 'country',)
    list_filter = ('country', 'city')
# Register your models here.
admin.site.register(Customer, CustomerAdmin)

