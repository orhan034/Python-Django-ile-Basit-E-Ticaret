# Generated by Django 4.1.5 on 2023-05-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='appMy.color', verbose_name='Renkler'),
        ),
    ]
