# Generated by Django 3.2 on 2021-04-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_alter_shop_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
