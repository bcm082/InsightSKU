# Generated by Django 5.0 on 2023-12-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insightskuapp', '0005_alter_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
