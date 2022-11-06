from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout

# URL fonksiyonlarını burada tanımla.

# Kayıt olma fonksiyonu
def register(request):
    
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        print("db ye kaydettim")
        auth_login(request,newUser)

        messages.success(request,"Başarıyla Kayıt Olundu...")
        print("kayıt oldum index e gidiyorum ")
        return redirect("index")
    context = {
        "form": form
    }
    
    return render(request, "register.html",context)

    """
    # POST metodunu manuel kontrol etmek için aşağıdaki metodu kullanabilirsin. 

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            login(request)

            return redirect("index")
        context = {
        "form": form
        }
        return render(request, "register.html",context)

    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "register.html",context)"""
    
# Giriş fonksiyonu
# authenticate fonksiyonu oturum açma işlemini gerçekleştirir
def login(request):

    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password= password)

        if user is None:
            messages.warning(request,"Kullanıcı Adı ve ya Parola Hatalı")
            return render(request,"login.html",context)
        
        
        
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        auth_login(request,user)
    
        return redirect("index")
    
    return render(request, "login.html",context)

# logout fonksiyonu oturumu sonlandırır
def logout(request):
    auth_logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")

    return redirect("index")