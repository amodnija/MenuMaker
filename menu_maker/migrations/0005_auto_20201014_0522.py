# Generated by Django 2.2 on 2020-10-14 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_maker', '0004_auto_20201014_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='net_wt',
            field=models.CharField(max_length=120, verbose_name='Net Weight'),
        ),
    ]
