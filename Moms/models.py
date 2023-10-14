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


class UnitRawMaterials(models.Model):
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.unit

    class Meta:
        db_table = 'UnitRawMaterials'
        verbose_name = 'UnitRawMaterial'
        verbose_name_plural = 'UnitRawMaterials'


class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    unit_raw_material = models.ForeignKey(UnitRawMaterials, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='RawMaterial')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'RawMaterial'
        verbose_name = 'RawMaterial'
        verbose_name_plural = 'RawMaterials'


class MomsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='moms_profiles', blank=True, null=True)
    home_number = models.CharField(max_length=20, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        db_table = 'Moms'
        verbose_name = 'Mom'
        verbose_name_plural = 'Moms'


class FoodsModel(models.Model):
    mom = models.ForeignKey(MomsModel, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    food_price = models.IntegerField()
    food_recipe = models.CharField(max_length=500)
    food_order = models.IntegerField(editable=False, default=0)
    raw_material = models.ManyToManyField(RawMaterial)
    # amount_raw_materials = models.IntegerField()
    food_photo = models.ImageField(upload_to='foods_picture')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.food_name

    class Meta:
        db_table = 'Foods'
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

