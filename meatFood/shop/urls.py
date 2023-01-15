from django.urls import path
from .views import index, cart_page

urlpatterns = [
    path('', index, name = 'home_page'),
    path('cart/', cart_page, name = 'cart_page'),
]
