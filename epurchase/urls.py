from django.conf.urls import patterns, include, url

from epurchase.views import HomeView, BuyView, RedirectView

urlpatterns = patterns('',
        url(r'^$', HomeView.as_view(), name='temp'),
        url(r'^buy/$', BuyView.as_view(), name='buy'),
        url(r'^test-redirect/$', RedirectView.as_view(), name='redirect'),
    )
