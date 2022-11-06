from django.contrib import admin
from .models import Ihas

# Admin panelindeki düzenlemeler,
# list_display = Oluşturduğun modeldeki kategorileri admin panelinde gösterir
# list_display_links = Oluşturduğun modeldeki kategorilere link verir
# search_fields = Amin paneline arama çubuğu oluşturur
# list_filter = Admin panelinde sağda görülen filtre mekanizmasını oluşturur

@admin.register(Ihas)
class IhasAdmin(admin.ModelAdmin):
    list_display = ["renter","brand", "weight", "category", "money","created_date"]
    list_display_links = ["renter","brand", "weight", "category", "money","created_date"]
    search_fields = ["brand", "weight", "category", "money","created_date"]
    list_filter = ["brand", "weight", "category", "money","created_date"]
    class Meta:
        model = Ihas