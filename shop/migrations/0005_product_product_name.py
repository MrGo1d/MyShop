# Generated by Django 4.0.1 on 2022-01-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(db_index=True, default=1, max_length=200),
            preserve_default=False,
        ),
    ]
