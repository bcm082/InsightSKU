# Generated by Django 5.0 on 2023-12-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insightskuapp', '0004_imagedetail_producttype_tag_remove_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=40),
        ),
    ]
