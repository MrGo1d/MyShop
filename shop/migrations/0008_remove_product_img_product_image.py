# Generated by Django 4.0.1 on 2022-02-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_image_alter_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
