# Generated by Django 4.2.2 on 2023-07-06 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appList', '0008_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlist',
            name='product',
        ),
    ]