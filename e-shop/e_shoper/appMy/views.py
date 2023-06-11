from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages

def basketCount(request):
    if request.user.is_authenticated:
        return ShopBasket.objects.filter(user = request.user)
    else:
        return None

def index(request):
    product = ProductStok.objects.all()[:6]
    context = {
        'shopbasket':basketCount(request),
        'product':product,
    }
    return render(request, 'index.html', context)

def shop(request):
    products = ProductStok.objects.all()
    context = {
        'products':products,
        'shopbasket':basketCount(request),
    }
    return render(request, 'shop.html', context)

def productDetail(request, slug):
    prodcts = ProductStok.objects.all()
    product = get_object_or_404(ProductStok, product__slug = slug)
    shopbasket = ShopBasket.objects.filter(user = request.user)
    products = Product.objects.get(slug = slug)
    comments = Comment.objects.filter(product=products)
    
    if request.method == 'POST':
        
        if request.POST.get("submit")=="button":
            color = request.POST.get("color")
            size = request.POST.get("size")
            try:
                count = int(request.POST.get("count"))
            except:
                return redirect("/productDetail/"+ slug +"/")
            if count > 0:
                prod = SizeLetter.objects.filter(product__slug = slug, color__styletitle=color, size__title=size)
                if prod.exists():
                    prod = prod.get()
                    price_all = prod.price * count
                    shopprod = ShopBasket.objects.filter(user = request.user,product_letter = prod)
                    if shopprod.exists():
                        shopprod = shopprod.get()
                        shopprod.count += count
                        shopprod.price_all += price_all
                        shopprod.save()
                    else:
                        shopb = ShopBasket(user = request.user, product_letter = prod, 
                                        price_all=price_all, count = count)              
                        shopb.save()
                    return redirect("/productDetail/"+ slug +"/")
                else:
                    messages.warning(request, 'Böyle bir ürün bulunmamaktadır!')
                    return redirect("/productDetail/"+ slug +"/")
        elif request.POST.get("submit") == "buttonComment"  and request.user.is_authenticated:
            title = request.POST.get("title")     
            email = request.POST.get("email")     
            text = request.POST.get("text")     
            star = request.POST.get("star") 
            prodct = Product.objects.get(slug = slug)  
            if star != "puan":
                    
                    comment = Comment(user=request.user,email = email, title=title,text=text,star=star,product=prodct)
                    comment.save()
                    return redirect("/productDetail/"+ slug +"/")
            else:
                context.update({"hata": "Puanlama yapmadınız!"})
            
    # SCTIPT ==================
    listprice = []
    listcolor = []
    listsize = []
    sizeprice = product.sizeletter.all()
    for i in range(len(sizeprice)):
        listprice.append(sizeprice[i].price)
        listcolor.append(sizeprice[i].color.styletitle)
        listsize.append(sizeprice[i].size.slug)
    # SCTIPT ==================
    
    context = {
        'product':product,
        'listprice':listprice,
        'listcolor':listcolor,
        'listsize':listsize,
        'shopbasket':shopbasket,
        "comments":comments,
        'products':products,
        'prodcts':prodcts,
    }
    return render(request, 'product-details.html', context)

def cart(request):
    shopbasket = ShopBasket.objects.filter(user = request.user)
    toplam = 0
    for i in shopbasket:
        toplam += i.price_all

    if request.method == "POST":
        for k,v in dict(request.POST).items():
            if k != "csrfmiddlewaretoken":
                shopb =  shopbasket.get(id=k[5:])
                try:
                   v[0] = int(v[0])
                except:
                    return redirect("cart")

                if v[0] == "0":
                    shopb.delete()

                elif v[0] > 0:
                    shopb.count = v[0]
                    shopb.price_all = shopb.product_letter.price * int(v[0])
                    shopb.save()
                    print(k[5:],v[0])
                else:
                    return redirect("cart")
        return redirect("cart")
 
    context = {
        'shopbasket':shopbasket,
        'toplam':toplam,
    }
    return render(request, 'cart.html', context)

def cartDelete(request,cid):
    shopbasket = ShopBasket.objects.get(id = cid)
    shopbasket.delete()
    return redirect("cart")


def contactUs(request):

    context = {
        'shopbasket':basketCount(request),
    }
    return render(request, 'contact-us.html', context)

def checkout(request):
   
    context = {
       'shopbasket':basketCount(request),
    }
    return render(request, 'checkout.html', context)

def blog(request):
    
    context = {
        'shopbasket':basketCount(request),
    }
    return render(request, 'blog.html', context)

def blogSingle(request):
    
    context = {
        'shopbasket':basketCount(request),
    }
    return render(request, 'blog-single.html', context)

def error(request):
    context = {}
    return render(request, '404.html', context)
