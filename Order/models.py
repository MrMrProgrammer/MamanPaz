from django.core.validators import MinValueValidator
from django.db import models
from BaseApp.models import User
from Moms.models import FoodsModel
from Moms.models import MomsModel


class Cart(models.Model):
    user = models.ForeignKey(MomsModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(FoodsModel)
    count = models.IntegerField(validators=[MinValueValidator(4)])
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.products) + " | " + str(self.count)

    # def save(self, *args, **kwargs):
    #     if isinstance(self.date, date2jalali):
    #         self.date = self.date.togregorian()
    #     super().save(*args, **kwargs)

    class Meta:
        db_table = 'Order'
