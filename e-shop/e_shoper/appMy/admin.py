from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','id','user','category','stars')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','id','slug')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','id','slug')

@admin.register(SizeNumber)
class SizeNumberAdmin(admin.ModelAdmin):
    list_display = ('product','id','color','size','stok')

@admin.register(SizeLetter)
class SizeLetterAdmin(admin.ModelAdmin):
    list_display = ('product','id','color','stok')

@admin.register(ProductStok)
class ProductStokAdmin(admin.ModelAdmin):
    list_display = ('product','id')

@admin.register(Gander)
class GanderAdmin(admin.ModelAdmin):
    list_display = ('title','id','slug')

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('title','id','slug')

@admin.register(Size2)
class Size2Admin(admin.ModelAdmin):
    list_display = ('title','id','slug')

@admin.register(ProductImg)
class ProductImgAdmin(admin.ModelAdmin):
    list_display = ('product','id')

@admin.register(ShopBasket)
class ShopBasketAdmin(admin.ModelAdmin):
    list_display = ('user','product_letter','id','price_all','count')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ('user',"product", "id","title")



