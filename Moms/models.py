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


class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='RawMaterial')

    def __str__(self):
        return self.name


class UnitRawMaterials(models.Model):
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.unit


class MomsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='moms_profiles', blank=True, null=True)
    home_number = models.CharField(max_length=20, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class FoodsModel(models.Model):
    mom = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    food_price = models.IntegerField()
    food_order = models.IntegerField()
    food_recipe = models.CharField(max_length=500)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    unit_raw_material = models.ForeignKey(UnitRawMaterials, on_delete=models.CASCADE)
    amount_raw_materials = models.IntegerField()
    food_photo = models.ImageField(upload_to='foods_picture')

    def __str__(self):
        return self.food_name