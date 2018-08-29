from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    def get_abs_url(self):
        return reverse("shopRecycle:product_list_by_category", args=[self.category_name])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    added_date = models.DateTimeField("pub date")
    price = models.FloatField()
    count = models.IntegerField()
    color = models.TextField(choices=[("GR", "green"),("BL", "blue"),("WT", "white"),("BL", "black")])
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    should_be_on_main = models.BooleanField(default=False)

    def is_available(self):
        return self.count > 0

    def __str__(self):
        return self.product_name

    def get_abs_url(self):
        return reverse("shopRecycle:product_detail", args=[self.id])
