from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entree(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.FloatField()
    points = models.IntegerField(null=True)

    def __str__(self):
        return self.nom

class PlatPrincipal(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.FloatField()
    points = models.IntegerField(null=True)

    def __str__(self):
        return self.nom

class Fromage(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.FloatField()
    points = models.IntegerField(null=True)

    def __str__(self):
        return self.nom        

class Dessert(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.FloatField()
    points = models.IntegerField(null=True)

    def __str__(self):
        return self.nom

class Boisson(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.FloatField()
    points = models.IntegerField(null=True)

    def __str__(self):
        return self.nom   

class LieuRestauration(models.Model):
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)
    TYPE = (
     ('RU', 'Restaurant Universitaire'),
     ('BR', 'Brasserie'),
     ('CA', 'Cafétéria'),
     ('FO', 'Foodtruck'),
     ('SA', 'Salle administrative'),
     ('SW', 'Sandwicherie'),
    )
    typeR = models.CharField(null=True, max_length=2, choices=TYPE)
    codePostal = models.CharField(null=True, max_length=6)
    tempsAttente = models.IntegerField(null=True)
    note = models.FloatField(null=True)
    distance = models.FloatField(null=True)
    platPrincipal = models.ManyToManyField(PlatPrincipal, through='Menu')
    entree = models.ManyToManyField(Entree, through='Menu')
    fromage = models.ManyToManyField(Fromage, through='Menu')
    dessert = models.ManyToManyField(Dessert, through='Menu')
    boisson = models.ManyToManyField(Boisson, through='Menu')
    

    def __str__(self):
        return self.nom             

class Menu(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.FloatField()
    lieuRestauration = models.ForeignKey(LieuRestauration)
    platPrincipal = models.ForeignKey(PlatPrincipal)
    entree = models.ForeignKey(Entree, null=True)
    fromage = models.ForeignKey(Fromage, null=True)
    dessert = models.ForeignKey(Dessert, null=True)
    boisson = models.ForeignKey(Boisson, null=True)
    pain = models.NullBooleanField()

    def __str__(self):
        return self.nom

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ville = models.CharField(max_length=50)
    lieuEtude = models.CharField(max_length=50)
    solde = models.FloatField()

    def __str__(self):
        return self.solde

class Reservation(models.Model):
    user = models.OneToOneField(UserProfile)
    date = models.DateTimeField()
    menu = models.OneToOneField(Menu)

    def __str__(self):
        return self.date

