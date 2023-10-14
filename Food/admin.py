from django.contrib import admin
from . import models


admin.site.register(models.FoodsModel)
admin.site.register(models.UnitRawMaterials)
admin.site.register(models.RawMaterial)