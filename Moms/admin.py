from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.MomsModel)
admin.site.register(models.FoodsModel)
admin.site.register(models.State)
admin.site.register(models.City)
admin.site.register(models.UnitRawMaterials)
admin.site.register(models.RawMaterial)
