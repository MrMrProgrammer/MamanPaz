from django.db import models
from BaseApp.models import User
from Food.models import FoodsModel


# Create your models here.

class CompanyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_number = models.CharField(max_length=20)
    employee_count = models.IntegerField()

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'Company'


class CompanySchedule(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodsModel, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.company) + " | " + str(self.food)

    class Meta:
        db_table = 'CompanySchedule'
