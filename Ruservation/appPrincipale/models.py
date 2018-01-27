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
    
    def __str__(self):
        return self.nom 

class Regime(models.Model):
    vegetarien = models.NullBooleanField()
    vegan = models.NullBooleanField()

class Allergie(models.Model):
    sGluten = models.NullBooleanField()
    sLactose = models.NullBooleanField()


class Menu(models.Model):
    lieuRestauration = models.ForeignKey(LieuRestauration)
    date = models.DateField(null=True)
    platPrincipal = models.ManyToManyField(PlatPrincipal, through='MenuPlatPrincipal')
    entree = models.ManyToManyField(Entree, through='MenuEntree')
    fromage = models.ManyToManyField(Fromage, through='MenuFromage')
    dessert = models.ManyToManyField(Dessert, through='MenuDessert')
    boisson = models.ManyToManyField(Boisson, through='MenuBoisson')
    regime = models.ForeignKey(Regime, null=True)
    allergie = models.ForeignKey(Allergie, null=True)

    def __str__(self):
        return self.platPrincipal

class MenuFromage(models.Model):
    fromage = models.ForeignKey(Fromage)
    menu = models.ForeignKey(Menu)

class MenuEntree(models.Model):
    entree = models.ForeignKey(Entree)
    menu = models.ForeignKey(Menu)

class MenuPlatPrincipal(models.Model):
    platPrincipal = models.ForeignKey(PlatPrincipal)
    menu = models.ForeignKey(Menu)      

class MenuDessert(models.Model):
    dessert = models.ForeignKey(Dessert)
    menu = models.ForeignKey(Menu)

class MenuBoisson(models.Model):
    boisson = models.ForeignKey(Boisson)
    menu = models.ForeignKey(Menu)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ville = models.CharField(max_length=50)
    lieuEtude = models.CharField(max_length=50)
    solde = models.FloatField()
    regime = models.ForeignKey(Regime, null=True)
    allergie = models.ForeignKey(Allergie, null=True)


class Favoris(models.Model):
    user = models.ForeignKey(UserProfile)
    lieu = models.ForeignKey(LieuRestauration, null=True)

class Reservation(models.Model):
    prix = models.FloatField()
    user = models.ForeignKey(UserProfile)
    date = models.DateTimeField()
    menu = models.ForeignKey(Menu)
    pain = models.NullBooleanField()

    def __str__(self):
        return self.date
