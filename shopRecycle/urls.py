from django.conf.urls import url

from . import views

app_name = 'shopRecycle'
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^product_list/$', views.product_list, name='product_list'),
    url(r'^(?P<category_name>\w+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<product_id>[0-9]+)/detail/$', views.product_detail, name='product_detail'),
]
