# Generated by Django 4.2.5 on 2023-10-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Moms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodsmodel',
            name='raw_material',
            field=models.ManyToManyField(to='Moms.rawmaterial'),
        ),
        migrations.AlterModelTable(
            name='foodsmodel',
            table='Foods',
        ),
        migrations.AlterModelTable(
            name='momsmodel',
            table='Moms',
        ),
    ]
