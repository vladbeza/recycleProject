from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework import generics

from cart.cart import Cart
from news.models import NewPost, Author
from shopRecycle.models import Product
from cupon.models import Cupon
from shopRecycle.models import Category, Product


import sys


def news_short_list(request, count=3):
    news = NewPost.objects.all().order_by('pub_date')[:count]
    serializer = NewPostSerializer(news, many=True)
    return JsonResponse(serializer.data, safe=False)

class PostList(generics.ListCreateAPIView):
    queryset = NewPost.objects.all()
    serializer_class = NewPostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = NewPost.objects.all()
    serializer_class = NewPostSerializer


class CartView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        pdb.set_trace()
        cart = Cart(request)
        result = cart.cart
        result["discount"] = cart.get_discount()
        result["cupon"] = cart.cupon_id
        return JsonResponse(result)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            cart = Cart(request)
            try:
                product = Product.objects.get(pk=int(request.data["id"]))
            except Product.DoesNotExist:
                return HttpResponse(status=404)
            cart.add(product, int(request.data["count"]), bool(request.data["is_update"]))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def cart_delete(request, pk):
    cart = Cart(request)
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    cart.remove(product)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def cupon_view(request):
    serializer = CuponSerializer(data=request.data)
    if serializer.is_valid():
        try:
            now = timezone.now()
            cupon = Cupon.objects.get(code__iexact=serializer.data["code"],
                                      active_from__lte=now,
                                      active_to__gte=now,
                                      is_active=True)
            request.session["cupon_id"] = cupon.id
        except Cupon.DoesNotExist:
            request.session["cupon_id"] = None
            return Response("Invalid cupon code")
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def create_order_view(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def product_by_id(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ProductSerializer(product, context={"request": request})

    return JsonResponse(serializer.data)


class CategoriesList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductsCategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductsCategorySerializer