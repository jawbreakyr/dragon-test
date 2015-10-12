from django.contrib import admin

from epurchase.models import Buyer, Product, Transaction, Profile


admin.site.register(Profile)
admin.site.register(Buyer)
admin.site.register(Product)
admin.site.register(Transaction)
