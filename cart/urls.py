from django.conf.urls import url

from . import views

app_name = 'cart'
urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^remove/(?P<product_id>[0-9]+)/$', views.cart_remove, name='cart_remove'),
    url(r'^add/(?P<product_id>[0-9]+)/$', views.cart_add, name='cart_add')
]