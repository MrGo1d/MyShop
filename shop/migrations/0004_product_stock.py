# Generated by Django 4.0.1 on 2022-01-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_options_alter_product_index_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
