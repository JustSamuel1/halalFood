from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Product, OrderItem, Order, TeleAdmin
from .forms import CartForm
from .bot import bot
import os

# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'product': products,
               'title': 'Shop',
               }

    return render(request, 'shop/main.html', context)

def cart_page(request):
    if request.method == 'POST':
        received_form = CartForm(request.POST)
        print(request.POST)
        if received_form.is_valid():
            newOrder = Order()
            newOrder.first_name = request.POST['first_name']
            newOrder.last_name = request.POST['last_name']
            newOrder.phone_number = request.POST['phone_number']
            newOrder.user_address = request.POST['user_address']
            newOrder.comment = request.POST['comment']
            newOrder.save()

            received_slugs = request.POST['slugs_quantity']
            slugs = received_slugs.split('.')

            for item in slugs:
                item_slug = item[1:]
                item_quantity = int(item[0])
                newItem = OrderItem()
                newItem.order = newOrder
                newItem.product = Product.objects.get(slug=item_slug)
                newItem.quantity = item_quantity
                newItem.save()

            admin_list = TeleAdmin.objects.all()
            order_info = newOrder.get_order_info()
            for admin in admin_list:
                if admin.confirmed_admin:
                    bot.order_alarm(int(admin.chat_id), admin.name, order_info)

        else:
            print(received_form.errors)
            print(request.POST["slugs_quantity"])

        return HttpResponseRedirect('/')

    else:
        form = CartForm()
        context = { 'form': form,
                   }
        return render(request, 'shop/cart_page.html', context)
