from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori Adı"), max_length=50)
    slug = models.SlugField(("Slug Kategori"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(("Ürün Rengi"), max_length=50)
    styletitle = models.CharField(("Renk style"), max_length=50, null=True)
    slug = models.SlugField(("Slug Kategori"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Color, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title

class Gander(models.Model):
    title = models.CharField(("Cinsiyet"), max_length=50)
    slug = models.SlugField(("Slug Cinsiyet"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gander, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title

class Size(models.Model):
    # Ayakkabı
    title = models.CharField(("Ürün Bedeni"), max_length=50)
    slug = models.SlugField(("Slug Beden"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Size, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    image = models.ImageField(("Ürün resmi"), upload_to="product", null=True)
    title = models.CharField(("Başlık"), max_length=50)
    brand = models.CharField(("Marka"), max_length=50)
    text = models.TextField(("Açıklama"), max_length=1200)
    detail = models.TextField(("Özellikler"), max_length=1000)
    stars = models.FloatField(("Puan"), default=0)
    slug = models.SlugField(("Slug Title"), blank=True, null=True)
    colors = models.ManyToManyField(Color, verbose_name=("Renkler"))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    def __str__(self):
        return self.title
    
class ProductImg(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    image = models.ImageField(("Resim"), upload_to="product")

    def __str__(self):
        return self.product.title
# Ayakkabı
class SizeNumber(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name=("Beden"), on_delete=models.CASCADE)
    gander = models.ForeignKey(Gander, verbose_name=("Cinsiyet"), on_delete=models.CASCADE)
    price = models.FloatField(("Fiyat"), default=0)
    stok = models.IntegerField(("Stok Sayısı"), default=0)
    
    def __str__(self):
        return self.product.title
    
class Size2(models.Model):
    # s m l xl xxl
    title = models.CharField(("Ürün Bedeni"), max_length=50)
    slug = models.SlugField(("Slug Beden"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Size2, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
# Kıyafet
class SizeLetter(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
    size = models.ForeignKey(Size2, verbose_name=("Ürün Beden"), on_delete=models.CASCADE)
    gander = models.ForeignKey(Gander, verbose_name=("Cinsiyet"), on_delete=models.CASCADE)
    price = models.FloatField(("Fiyat"), default=0)
    stok = models.IntegerField(("Stok"), default=0)
    
    def __str__(self):
        return self.product.title + " || " + self.color.styletitle + " || " + self.size.title
    
class ProductStok(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    images = models.ManyToManyField(ProductImg, verbose_name=("Ürün fotografları"))
    sizenumber = models.ManyToManyField(SizeNumber, verbose_name=("Ayakkabı Beden ve Stok"), blank=True)
    sizeletter = models.ManyToManyField(SizeLetter, verbose_name=("Kıyafet Beden ve Stok"), blank=True)
    
    def __str__(self):
        return self.product.title
    
class ShopBasket(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    product_letter = models.ForeignKey(SizeLetter, verbose_name=("Ürün Giyisi"), on_delete=models.CASCADE)
    price_all = models.FloatField(("Toplam Fiyat"), default=0)
    count = models.IntegerField(("Adet"), default=0)

    def __str__(self):
        return self.product_letter.product.title


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    email = models.EmailField(("Email"), max_length=254, null=True)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    date = models.DateField(("Saat"), auto_now_add=True)
    time = models.TimeField(("Tarih"), auto_now_add=True)
    text = models.TextField(("Yorum"), max_length=1000)
    star = models.IntegerField(("Yorum Puanı"), default=0)

    def __str__(self):
        return self.title


