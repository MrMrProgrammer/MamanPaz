from django.db import models
from BaseApp.models import User


class State(models.Model):
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.state


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.city


class MomsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='moms_profiles', blank=True, null=True)
    home_number = models.CharField(max_length=20, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        db_table = 'Moms'
        verbose_name = 'Mom'
        verbose_name_plural = 'Moms'
