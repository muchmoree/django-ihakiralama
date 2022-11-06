from django import forms
from .models import Ihas


# Oluşturduğum modelin önyüzde görünmesine yardımcı olur

class ihaFrom(forms.ModelForm):
    class Meta:
        model = Ihas
        fields = ["brand","weight","category","money","iha_image"]
