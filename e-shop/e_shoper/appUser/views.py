from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def loginUser(request):
    if request.method == 'POST':
        if request.POST.get("submit")=="buttonGiris":
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            harfet = False
            for harf in username:
                if harf == "@":
                    harfet = True
            if username[-4:] == ".com" and harfet: 
                try:
                    user = User.objects.get(email=username)
                    username = user.username
                except:
                    messages.warning(request, 'Email hatalı!')
                    return redirect("loginUser")

            user = authenticate(username = username, password=password)
            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                messages.warning(request, 'Kullanıcı Adı veya Şifre Hatalı!')
                return redirect("loginUser")
        
        if request.POST.get("submit")=="buttonKayit":
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
             
            harfup = False
            harfnum = False
            if password1 == password2:
                for harf in password1:
                    if harf.isupper():
                        harfup = True
                    if harf.isnumeric():
                        harfnum = True
                if harfup and harfnum and len(password1)>=6:
                    if not User.objects.filter(username=username).exists():
                        if not User.objects.filter(email=email).exists():
                            user = User.objects.create_user(username=username,
                                                            password=password1,
                                                            email=email,
                                                            first_name=name,
                                                            last_name=surname)    
                            user.save()
                            return redirect("loginUser")
                        else:
                            messages.warning(request, 'Bu email zaten kullanılıyor!')
                            return redirect("loginUser")
                    else:
                        messages.warning(request, 'Kullanıcı Adı zaten kullanılıyor!')
                        return redirect("loginUser")
                else:
                    messages.warning(request, 'Şifreler aynı değil!')
                    messages.warning(request, 'Şifre en az 6 karakter içermelidir!')
                    messages.warning(request, 'Şifre en az bir büyük harf içermelidir!')
                    return redirect("loginUser")
           
    context = {}
    return render(request, 'user/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect("index")