from django.contrib import admin
from .models import Order, Transaction


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__user__username', 'product__name')   # ✅ search by Customer username


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'method', 'successful', 'transaction_date')
    list_filter = ('method', 'successful', 'transaction_date')
    search_fields = ('order__id', 'method')
