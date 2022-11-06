from django.contrib import admin
from django.urls import path,include
from ihas import views
from django.conf import settings
from django.conf.urls.static import static


# Uygulamada gidecek URL'leri burada tanımla
# Proje içinde uygulama kurulduğunda nested url tanımı için "include" fonksiyonu kullan
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('ihas/', include("ihas.urls")),
    path('user/', include("user.urls")),
]

# Media klasörünün yolunu aşağıdaki gibi ver
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
