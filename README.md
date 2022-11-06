# Django - Ürün Yönetim Sistemi
Sistem basit bir arayüze sahip olup, kullanıcı girişlerinin olduğu ve ürünlerinizin modellenip kullanıcılara gösterildiği, ürünleri güncelleme ve silme gibi fonksiyonları barındıran bir django uygulamasıdır.

### Kullanılan Uygulamalar
-Django <br/>
-Python <br/>
-Postgresql

## Hadi Başlayalım
Adım-1) Öncelikle projeyi çalışmak istediğiniz yere klonlayın. <br/>
Adım-2) Python ile pip indirin ve projenin gerekli kütüphanelerini sırasıyla kurun. Gerekli kütüphaneler aşağıdadır. <br/>

[Python](https://www.python.org/downloads/) linkinden sisteminize uygun sürümü bulabilirsiniz.

`pip install --upgrade-pip` <br/>
`pip install Django==4.1.3` Sürüm değişiklikleri olabilir. <br/>
`pip install Pillow` <br/>
`pip install django-crispy-forms` <br/>
`pip install django-cleanup` <br/>
`pip install psycopg2` <br/>

Adım-3) Link üzerinden bilgisayarınıza göre uygun sürümü seçip [postgresql](https://www.postgresql.org/download/) bilgisayarınıza kurun. <br/>
Adım-4) Postgresql'i bilgisayarınıza kurarken database ismini, port numarasını ve varsayılan olarak gelen postgres kullanıcı adının şifresini 
iharent > `setting.py` > DATABASES kısmı ile eşleştirin. <br/>

Adım-5) Klasör dizininde bir terminal açıp `python manage.py createsuperuser` komutunu girip usernam,email ve şifre belirleyerek 
bir admin kullanıcısı oluşturun. <br/>

Adım-6) Database modellerinin postgresql database'ine işlenmesi için sırasıyla bu komutları çalıştırın 
--> `python manage.py makemigrations` ve `python manage.py migrate` <br/>

Adım-7) Herhangi bir hata ile karşılaşmadıysanız artık uygulama kullanıma hazır demektir. `python manage.py runserver`
komutunu çalıştırarak local sunucunuzu ayağa kaldırın ve [Sunucu](https://127.0.0.1:8000) linkinden sistemi görüntüleyebilirsiniz. <br/>

## Proje Görselleri
Anasayfa
![Anasayfa](https://github.com/muchmoree/django-ihakiralama/blob/master/projegeneralimages/anasayfa.png)
Dashboard
![Dashboard](https://github.com/muchmoree/django-ihakiralama/blob/master/projegeneralimages/dashboard.png)
Ürünler
![Ihalar](https://github.com/muchmoree/django-ihakiralama/blob/master/projegeneralimages/ihalar.png)
Ürün Güncelle
![UrunGuncelle](https://github.com/muchmoree/django-ihakiralama/blob/master/projegeneralimages/urunguncelle.png)
Ürün Ekle
![UrunEkle](https://github.com/muchmoree/django-ihakiralama/blob/master/projegeneralimages/urunekle.png)
Giriş Yap
![GirisYap](https://github.com/muchmoree/django-ihakiralama/blob/master/projegeneralimages/girisyap.png)
Kayıt Ol
![KayitOl](https://github.com/muchmoree/django-ihakiralama/blob/master/projegeneralimages/kayıtol.png)

## Teşekkürler
