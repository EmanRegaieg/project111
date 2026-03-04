from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator
class Categorie(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
     return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=30)
    date_publication = models.DateField()
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL,
    null=True)
    resume = models.TextField()
    nombre_pages = models.IntegerField(validators=[MinValueValidator(1)])
    couverture = models.ImageField(upload_to='couvertures/', null=True,
    blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['-date_ajout']
    
    def __str__(self):
     return self.titre