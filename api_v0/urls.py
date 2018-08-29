from django.conf.urls import url
from .views import *

app_name = 'api_v0'
urlpatterns = [
    url(r'^news/$', news_short_list),
    url(r'^news_all/$', PostList.as_view()),
    url(r'^news/(?P<pk>[0-9]+)/$', PostDetail.as_view()),
    url(r'^cart/$', CartView.as_view()),
    url(r'^cart/(?P<pk>[0-9]+)/$', cart_delete),
    url(r'^cupon/$', cupon_view),
    url(r'^crete_order/$', create_order_view, name="create-order"),
    url(r'^product/(?P<pk>[0-9]+)/$', product_by_id, name="product-detail"),
    url(r'^categories/$', CategoriesList.as_view(), name="categories-list"),
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryDetail.as_view(), name="category-detail")
]
