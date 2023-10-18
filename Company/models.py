from django.db import models


# Create your models here.

class CompanyModel(models.Model):
    company_name = models.CharField(max_length=100)
    company_number = models.CharField(max_length=20)
    employee_count = models.IntegerField()

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'Company'
