from rest_framework import serializers
from news.models import NewPost, Author
from cupon.models import Cupon
from orders.models import Order, OrderItem
from orders.tasks import order_created
from cart.cart import Cart
from shopRecycle.models import Category, Product
import pdb


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('nick_name', 'posts')


class NewPostSerializer(serializers.ModelSerializer):
   author = AuthorSerializer()
   class Meta:
       model = NewPost
       fields = [
           'id',
           'title',
           'short_image',
           'pub_date',
           'author',
           'image',
           'text',
       ]

class CuponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cupon
        fields = ['Cupon']


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.CharField(source='get_total_price')

    class Meta:
        model = Order
        fields = ['first_name',
                  'last_name',
                  'email',
                  'address',
                  'city',
                  'created',
                  'updated',
                  'total_price']

    def create(self, validated_data):
        cart = Cart(self.context["request"])
        if cart.cupon:
            validated_data["cupon"] = cart.cupon
            validated_data["discount"] = cart.cupon.discount
        order = Order.objects.create(**validated_data)
        for item in cart:
            OrderItem.objects.create(order=order, product=item["product"],
                                     price=item["price"], quantity=item["count"])
            cart.clear()
        order_created.delay(order.id)
        return order


class CartSerializer(serializers.Serializer):

    def to_internal_value(self, data):
        for key in ("id", "count", "is_update"):
            value = data.get(key)
            if value is None:
                raise serializers.ValidationError("{} key wasn't found".format(key), code=None)
        return data


class ProductsCategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:category-detail'
        )
    products = serializers.HyperlinkedRelatedField(many=True, view_name='api:product-detail', read_only=True)

    class Meta:
        model = Category
        fields = ["url", "id", "category_name", "category_description", "products"]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:product-detail',
        lookup_field='pk',
        )

    class Meta:
        model = Product
        fields = ["url",
                  "id",
                  "product_name",
                  "product_description",
                  "added_date",
                  "price",
                  "count",
                  "color",
                  "image",]

