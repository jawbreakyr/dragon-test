from django.db import models
from django.contrib.auth.models import User


TRANSACTION_STATUS = (
    (0, 'Pending'),
    (1, 'Completed'),
    (2, 'Rejected'),
    (3, 'Returned'),
)


class Profile(models.Model):
    owner = models.OneToOneField(User, related_name='profile')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "{0}, {1}".format(self.first_name, self.last_name)


class Buyer(Profile):
    balance = models.IntegerField(default=0)

    def __str__(self):
        return "{0}, {1}".format(self.first_name, self.balance)


class Transaction(models.Model):
    owner = models.ForeignKey(Buyer, related_name='transaction')
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.owner)


class Product(models.Model):
    transaction = models.ForeignKey(Transaction, related_name='item', null=True, blank=True)
    cost = models.IntegerField(default=0)
    name = models.CharField(max_length=50, blank=False)
    seller = models.ForeignKey(Profile, related_name='product')

    def __str__(self):
        return "{0}".format(self.name)
