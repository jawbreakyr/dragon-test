from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.conf import settings
from uuid import uuid4

from ecommerce.dragonpay import DragonPay
from epurchase.forms import ProductForm
from epurchase.models import Product


class HomeView(TemplateView):
    template_name = 'epurchase/test.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all()

        return context


class BuyView(View):

    def post(self, request, *args, **kwargs):
        print request.GET
        print request.POST
        dp = DragonPay(merchant=settings.MERCHANT_ID, password=settings.PASSWORD)
        url = dp.pay(
            transaction_id=uuid4(), amount='1000000', currency='PHP',
            description='churva', email='sample@example.com')
        return HttpResponseRedirect(url)


class RedirectView(TemplateView):

    def get(self, *args, **k):
        pass