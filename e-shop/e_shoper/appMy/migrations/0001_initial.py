# Generated by Django 4.1.5 on 2023-05-30 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kategori Adı')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Ürün Rengi')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Gander',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Cinsiyet')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Cinsiyet')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('brand', models.CharField(max_length=50, verbose_name='Marka')),
                ('text', models.TextField(max_length=1200, verbose_name='Açıklama')),
                ('detail', models.TextField(max_length=1000, verbose_name='Özellikler')),
                ('stars', models.FloatField(default=0, verbose_name='Puan')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='Kategori')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Ürün Bedeni')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Beden')),
            ],
        ),
        migrations.CreateModel(
            name='Size2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Ürün Bedeni')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Beden')),
            ],
        ),
        migrations.CreateModel(
            name='SizeNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Fiyat')),
                ('stok', models.IntegerField(default=0, verbose_name='Stok Sayısı')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.color', verbose_name='Renk')),
                ('gander', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.gander', verbose_name='Cinsiyet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.size', verbose_name='Beden')),
            ],
        ),
        migrations.CreateModel(
            name='SizeLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Fiyat')),
                ('stok', models.IntegerField(default=0, verbose_name='Stok')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.color', verbose_name='Renk')),
                ('gander', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.gander', verbose_name='Cinsiyet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.size2', verbose_name='Ürün Beden')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('size', models.ManyToManyField(blank=True, to='appMy.sizeletter', verbose_name='Kıyafet Beden ve Stok')),
                ('sizenumber', models.ManyToManyField(blank=True, to='appMy.sizenumber', verbose_name='Ayakkabı Beden ve Stok')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product', verbose_name='Resim')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
            ],
        ),
    ]
