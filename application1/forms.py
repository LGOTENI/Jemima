#from django.forms import ModelForm
from django import forms
from  application1 import models
from .models import Produit, Categorie


class CategorieForm(forms.ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('nom_categorie', 'description')
        
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ('nom', 'categorie', 'prix', 'quantite', 'image')
