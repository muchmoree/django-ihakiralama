from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from ihas.models import Ihas
from .forms import ihaFrom
from django.contrib.auth.decorators import login_required


# URL fonksiyonlarını burada tanımla.
# login_required decorator kullanarak oturum session yönetebilirsin.
# İlgili sayfalarda gerekli CRUD işlemlerini yap. 
# Ulaşılmaması gerekilen URL'ler için get_object_or_404 metodunu kullanabilirsin.

# Ürün listeleme fonksiyonu
def ihas(request):
    # Arama özelliği
    keyword = request.GET.get("keyword")
    if keyword:
        ihas = Ihas.objects.filter( brand__contains = keyword) | Ihas.objects.filter( money__contains = keyword) | Ihas.objects.filter( category__contains = keyword) | Ihas.objects.filter( weight__contains = keyword)
        return render(request,"ihas.html",{'ihas':ihas})
        
    # Filtreleme işlemi de arama ile aynıdır.
    ihas = Ihas.objects.all()
    return render(request,"ihas.html",{'ihas':ihas})

# Anasayfa fonksiyonu
def index(request):
    return render(request,"index.html")

# Üye kontrol paneli fonksiyonu
@login_required(login_url= "user:login")
def dashboard(request):
    ihas = Ihas.objects.filter(renter = request.user)
    context = {
        "ihas":ihas
    }
    return render(request,"dashboard.html",context)

# Ürün ekleme fonksiyonu
@login_required(login_url= "user:login")
def addiha(request):
    form = ihaFrom(request.POST or None,request.FILES or None)

    if form.is_valid():
        iha = form.save(commit=False)
        iha.renter = request.user
        iha.save()
        messages.success(request,"Iha başarıyla eklendi...")
        return redirect("ihas:dashboard")

    return render(request,"addiha.html",{"form":form})

# Ürün güncelleme fonksiyonu
@login_required(login_url= "user:login")
def updateiha(request,id):

    iha = get_object_or_404(Ihas,id = id)
    form = ihaFrom(request.POST or None,request.FILES or None, instance=iha)

    if form.is_valid():
        iha = form.save(commit=False)
        iha.renter = request.user
        iha.save()
        messages.success(request,"Iha başarıyla güncellendi...")
        return redirect("ihas:dashboard")

    return render(request,"update.html",{"form":form})

# Ürün silme fonksiyonu
@login_required(login_url= "user:login")
def deleteiha(request,id):
    iha = get_object_or_404(Ihas,id = id)

    iha.delete()

    messages.success(request,"Ürün silindi")

    return redirect("ihas:dashboard")