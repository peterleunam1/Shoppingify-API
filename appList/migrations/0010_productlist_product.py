# Generated by Django 4.2.2 on 2023-07-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appList', '0009_remove_productlist_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='product',
            field=models.ManyToManyField(to='appList.product'),
        ),
    ]
