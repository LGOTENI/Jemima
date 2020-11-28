from django.db import models
from django.utils import timezone
#from django.contrib import admin

class Tables(models.Model):
    pass
    class Meta:
        abstract = True
class Categorie(Tables):
    nom_categorie=models.CharField(max_length=200, null=False)
    description=models.TextField()
      
    def __str__(self):
        return self.nom_categorie
    
class Produit(Tables):
    nom=models.CharField(max_length=200, blank=False)
    categorie=models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix=models.IntegerField()
    quantite=models.IntegerField()
    date_creation  =  models.DateTimeField(default=timezone.now(), blank=True, verbose_name="Date création") 
    image=models.FileField(upload_to='img')
    def __str__(self):
        return self.nom
