from django.contrib import admin
from django.urls import path,include
from . import views

# Uygulama içinde uygulama oluşturursan app_name yazmak zorundasın.
app_name = "ihas"

# Oluşturduğun yeni uygulama URL' lerini aşağıdaki gibi verebilirsin.
# Name değişkenine göre gideceğin yeri referanslayabilirsin.
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addiha/', views.addiha, name="addiha"),
    path('update/<int:id>', views.updateiha, name="update"),
    path('delete/<int:id>', views.deleteiha, name="delete"),
    path('', views.ihas, name="ihas"),

]