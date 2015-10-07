from django.conf.urls import patterns, include, url

from epurchase.views import HomeView, BuyView

urlpatterns = patterns('',
        url(r'^$', HomeView.as_view(), name='temp'),
        url(r'^buy/$', BuyView.as_view(), name='buy'),
    )
