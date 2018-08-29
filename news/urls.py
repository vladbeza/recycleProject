from django.conf.urls import url
from . import views

app_name = 'news'
urlpatterns = [
        url(r'^all/$', views.posts_list, name='posts_list'),
        url(r'^blog_detail/(?P<blog_id>\d+)/$', views.post_details, name='post_details'),
        ]