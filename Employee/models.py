from django.db import models
from BaseApp.models import User
from Company.models import CompanyModel


# Create your models here.


class EmployeeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " | " + self.company.company_name

    class Meta:
        db_table = 'Employee'
