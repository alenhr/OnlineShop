from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import django

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.now())
    # key_expires = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'

# class Product(models.Model):
# 	title = models.CharField(max_length=120)
# 	description = models.TextField(null=True, blank=True)
# 	price = models.DecimalField(default=10.99, max_digits=100, decimal_places=2)
# 	sale_price = models.DecimalField(default=10.99, max_digits=100, decimal_places=2)
# 	timestamp = models.DateTimeField()
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
# 	active = models.BooleanField(default=True)
# 	update_defaults = models.BooleanField(default=False)

# 	def __unicode__(self):
# 		return self.title

# 	def get_price(self):
# 		return self.price

# class CartItem(models.Model):
# 	cart = models.ForeignKey('Cart', null=True, blank=True)
# 	product = models.ForeignKey(Product)
# 	quantity = models.IntegerField(default=1)
# 	line_total = models.DecimalField(default=10.99, max_digits=100, decimal_places=2)
# 	notes = models.TextField(null=True, blank=True)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

# 	def __unicode__(self):
# 		try:
# 			return str(self.cart.id)
# 		except:
# 			return self.product.title


# class Cart(models.Model):
# 	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
# 	active = models.BooleanField(default=True)

# 	def __unicode__(self):
# 		return "Cart id: %s" %(self.id)

