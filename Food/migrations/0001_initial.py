# Generated by Django 4.2.5 on 2023-10-14 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Moms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitRawMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'UnitRawMaterial',
                'verbose_name_plural': 'UnitRawMaterials',
                'db_table': 'UnitRawMaterials',
            },
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='RawMaterial')),
                ('unit_raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food.unitrawmaterials')),
            ],
            options={
                'verbose_name': 'RawMaterial',
                'verbose_name_plural': 'RawMaterials',
                'db_table': 'RawMaterial',
            },
        ),
        migrations.CreateModel(
            name='FoodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('food_price', models.IntegerField()),
                ('food_recipe', models.CharField(max_length=500)),
                ('food_order', models.IntegerField(default=0, editable=False)),
                ('food_photo', models.ImageField(upload_to='foods_picture')),
                ('is_active', models.BooleanField(default=True)),
                ('mom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Moms.momsmodel')),
                ('raw_material', models.ManyToManyField(to='Food.rawmaterial')),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
                'db_table': 'Foods',
            },
        ),
    ]
