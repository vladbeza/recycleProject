"""recycleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include("cart.urls", namespace="cart")),
    url(r'^order/', include("orders.urls", namespace="orders")),
    url(r'^cupon/', include("cupon.urls", namespace="cupon")),
    url(r'^api/v0/', include('api_v0.urls', namespace="api")),
    url(r'^blog/', include('news.urls', namespace="blog")),
    url(r'^', include('shopRecycle.urls', namespace="shopRecycle")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^auth/', include('core.urls', namespace="core")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
