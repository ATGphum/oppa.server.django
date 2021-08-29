# Generated by Django 3.2.5 on 2021-08-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppaapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=1),
        ),
    ]