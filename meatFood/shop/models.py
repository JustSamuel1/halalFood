from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Product(models.Model):
    name = models.CharField(max_length=30)
    weight = models.FloatField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='photos')
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(200, 100)],
                                     format='JPEG',
                                     options={'quality': 60})
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    user_address = models.CharField(max_length=150, blank=False)
    comment = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created', ]
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_order_info(self):
        order_info = '*{0} {1}* has made an order!\n' \
                     'Tel: *{2}*\n' \
                     'Address: *{3}*\n\n' \
                     'Order details:\n'.format(self.first_name, self.last_name, self.phone_number, self.user_address)

        for item in self.items.all():
            item_coast = item.get_cost()
            total_coast = self.get_total_cost()
            order_info += "*{0}*, quantity: *{1}*, for coast *{2}$*. " \
                          "Slug: *{3}*\n".format(item.product.name, item.quantity, item_coast,
                                                 item.product.slug)
        order_info += "Total coast: *{}$*\n".format(total_coast)
        order_info += '\nWith a comment:\n{}'.format(self.comment)
        return order_info


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.product.price * self.quantity


class TeleAdmin(models.Model):
    name = models.CharField(max_length=50, blank=False)
    chat_id = models.CharField(max_length=15, blank=False)
    confirmed_admin = models.BooleanField(default=False)
