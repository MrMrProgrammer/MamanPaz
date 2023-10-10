from django.core.validators import MinValueValidator
from django.db import models
from BaseApp.models import User
from Moms.models import FoodsModel
from Moms.models import MomsModel


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    payment_data = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        db_table = 'Order'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodsModel, on_delete=models.CASCADE)
    final_price = models.IntegerField(null=True, blank=True)
    count = models.IntegerField()

    def __str__(self):
        return str(self.order) + " | " + str(self.food) + " | " + str(self.count)