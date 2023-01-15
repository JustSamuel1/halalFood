from django.contrib import admin
from .models import Product, Order, OrderItem, TeleAdmin
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user_address', 'get_total_cost']

class TeleAdminAdmin(admin.ModelAdmin):
    list_display = ['name', 'chat_id']


admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(TeleAdmin, TeleAdminAdmin)


