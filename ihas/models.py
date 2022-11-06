from django.db import models


class Ihas(models.Model):
    
    # Uygulamanın amacına göre istediğin özellikler modelde modellenir.
    # İhtiyaç olunanlar: kiralayan, marka, model, ağırlık, kategori, fiyat ve yaratılma tarihi

    renter = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Kiralayan")
    brand = models.CharField(max_length=40,verbose_name="Marka")
    weight = models.CharField(max_length=6, verbose_name="Ağırlık")
    category = models.CharField(max_length=20, verbose_name="Kategori")
    money = models.IntegerField(verbose_name="Fiyat")
    iha_image = models.FileField(blank=True, null=True, verbose_name="Ürün Fotoğrafı Seç")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulan Tarih")


# Admin panaelinde hangi kategori ismi ile gruplandığını görmek için aşağıdaki fonksiyonu kullan
# Bunu Meta class'ının üzerinde yazabilirsin
#def __str__(self):
#   return self.brand