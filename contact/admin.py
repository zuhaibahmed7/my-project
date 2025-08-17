from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'subject', 'created_at')
    list_display=('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)



# Register your models here.
admin.site.register(ContactMessage, ContactMessageAdmin)

