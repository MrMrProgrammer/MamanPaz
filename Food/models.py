from django.db import models
from Moms.models import MomsModel


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


class FoodsModel(models.Model):
    mom = models.ForeignKey(MomsModel, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    food_price = models.IntegerField()
    food_recipe = models.CharField(max_length=500)
    food_order = models.IntegerField(editable=False, default=0)
    # raw_material = models.ManyToManyField(RawMaterial, blank=True, null=True)
    # amount_raw_materials = models.IntegerField()
    food_photo = models.ImageField(upload_to='foods_picture')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.food_name

    class Meta:
        db_table = 'Foods'
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
