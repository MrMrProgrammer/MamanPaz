from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_active_code = models.CharField(max_length=100, null=True, blank=True)
    is_mom = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'User'