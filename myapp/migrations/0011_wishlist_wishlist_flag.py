# Generated by Django 4.1.3 on 2022-12-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_product_product_genral_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='wishlist_flag',
            field=models.BooleanField(default=False),
        ),
    ]