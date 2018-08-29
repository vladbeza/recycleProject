from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cupon(models.Model):

    code = models.CharField(verbose_name='code', max_length=50)
    active_from = models.DateTimeField()
    active_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    is_active = models.BooleanField()

    def __str__(self):
        return self.code