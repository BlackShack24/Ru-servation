from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Ruservation.forms import SignUpForm, ParamForm
from appPrincipale.models import LieuRestauration, Menu, MenuPlatPrincipal, PlatPrincipal, UserProfile, Favoris, Regime, Allergie, Reservation
from datetime import datetime
# Create your views here.

# Renvoie vers le formulaire d'inscription
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'appPrincipale/signup.html', {'form': form})

# Renvoie vers la page home qui permet la affichage et la recherchere des lieux de restauration
def home(request):
    userProfil = UserProfile.objects.all()
    lieux = LieuRestauration.objects.all()
    fav = Favoris.objects.all()
    menu = Menu.objects.all()
    menupp = MenuPlatPrincipal.objects.all()
    platPrincipal = PlatPrincipal.objects.all()
    re = Regime.objects.all()
    al = Allergie.objects.all()
    return render(request, 'appPrincipale/home.html', {'lieux': lieux, 'fav' : fav, 'menu' : menu, 'menupp' : menupp, 'pp' : platPrincipal, 're' : re, 'al' : al, 'userProfil' : userProfil})

# Renvoie vers la page du lieu de restauration selectionné, vérifie si ce lieu est dans les favoris ou non
def lieuR(request, lieu_id, user_id):
    lieu = LieuRestauration.objects.get(pk=lieu_id)
    menu = get_object_or_404(Menu, lieuRestauration_id = lieu.id)
    menupp = MenuPlatPrincipal.objects.filter(menu_id = menu.id)
    platPrincipal = PlatPrincipal.objects.all()
    if(Favoris.objects.filter(lieu_id=lieu_id, user_id=user_id).count()>0): fav = True;
    else: fav = False; 
    return render(request, 'appPrincipale/lieu.html', {'lieu': lieu, 'menu': menu, 'plats': platPrincipal, 'menupp': menupp, 'fav' : fav})

# Renvoie vers la page profil, si c'est la première fois que l'utilisateur accède à cette page, un UserProfil sera créé avec des valeurs par défaut
def profil(request, user_id):
    if UserProfile.objects.filter(user_id=user_id).count() == 0:
        userProfil = UserProfile(ville='Nancy', lieuEtude='ARTEM', solde=0, user_id=user_id)
        regimes = Regime(vegetarien=False, vegan=False)
        regimes.save()
        userProfil.regime_id = regimes.id
        allergies = Allergie(sGluten=False, sLactose=False)
        allergies.save()
        userProfil.allergie_id = allergies.id    
        userProfil.save()
    else:
        userProfil = UserProfile.objects.get(user_id=user_id)
        regimes = Regime.objects.get(pk=userProfil.regime_id)
        allergies = Allergie.objects.get(pk=userProfil.allergie_id)
    return render(request, 'appPrincipale/profil.html', {'userProfil': userProfil, 're' : regimes, 'al' : allergies})

# Cette vue ajoute le lieu de restauration selectionné aux favoris, si il y est déja il sera alors supprimé des favoris
def addFav(request, lieu_id, user_id):
    if Favoris.objects.filter(user_id=user_id, lieu_id=lieu_id).count()>0:
        Favoris.objects.filter(user_id=user_id, lieu_id=lieu_id).delete()
    else:
        f = Favoris(user_id=user_id, lieu_id=lieu_id)
        f.save()
    return redirect('favoris', user_id = user_id) 

# Renvoie vers la page favoris
def favoris(request, user_id):
    userP = UserProfile.objects.get(user_id=user_id)
    fav = Favoris.objects.filter(user_id=user_id).values_list('lieu_id', flat='True')
    lieux = LieuRestauration.objects.filter(id__in = fav)
    return render(request, 'appPrincipale/favoris.html', {'lieux' : lieux, 'userP' : userP})

# Renvoie vers la page parametres, si c'est la première fois que l'utilisateur accède à cette page 
# une nouvelle entrée sera créé dans les tables Regimes et Allergies avec des valeurs par défaut (false) 
def parametres(request, user_id):
    userP = UserProfile.objects.get(user_id=user_id)
    if UserProfile.objects.filter(user_id=user_id, regime_id__isnull=True):
        r = Regime(vegetarien=False, vegan=False)
        r.save()
        userP.regime_id = r.id
        userP.save()
    if UserProfile.objects.filter(user_id=user_id, allergie_id__isnull=True):
        a = Allergie(sGluten=False, sLactose=False)
        a.save()
        userP.allergie_id = a.id    
        userP.save()
    re = Regime.objects.get(pk=userP.regime_id)
    al = Allergie.objects.get(pk=userP.allergie_id)
    return render(request, 'appPrincipale/parametres.html', {'userP' : userP, 're' : re, 'al' : al})

# Cette vue enregistre les modifications apportées sur le formulaire de la page parametres dans la BDD
def get_Param(request, user_id):
    form = ParamForm(request.POST)
    if form.is_valid():
        userProfil = UserProfile.objects.get(user_id=user_id)
        al = Allergie.objects.get(pk=userProfil.allergie_id)
        re = Regime.objects.get(pk=userProfil.regime_id)
        userProfil.ville = form.cleaned_data['ville']
        userProfil.lieuEtude = form.cleaned_data['etab']
        al.sGluten = form.cleaned_data['sGluten']
        al.sLactose = form.cleaned_data['sLactose']
        re.vegetarien = form.cleaned_data['vegetarien']
        re.vegan = form.cleaned_data['vegan']
        userProfil.save()
        al.save()
        re.save()
    return redirect('profil', user_id = user_id)

# Renvoie vers la page de géolocalisation d'un lieu
def geoLoc(request, lieu_id):
    lieu = LieuRestauration.objects.get(pk=lieu_id)
    return render(request, 'appPrincipale/geoLoc.html', {'lieu': lieu})

# Renvoie vers la page de réservation d'un menu
def reservation(request, lieu_id, user_id):
    lieu = LieuRestauration.objects.get(pk=lieu_id)
    userP = UserProfile.objects.get(user_id=user_id)
    menu = get_object_or_404(Menu, lieuRestauration_id = lieu.id)
    menupp = MenuPlatPrincipal.objects.filter(menu_id = menu.id)
    platPrincipal = PlatPrincipal.objects.all()
    return render(request, 'appPrincipale/reservation.html', {'lieu': lieu, 'userP' : userP, 'menu': menu, 'plats': platPrincipal, 'menupp': menupp})

# Renvoie vers la page historique
def historique(request, user_id):
    res = Reservation.objects.filter(user_id=user_id)
    lieu = LieuRestauration.objects.all()
    return render(request, 'appPrincipale/historique.html', {'res': res, 'lieu' : lieu})

# Cette vue créée ajoute une nouvelle réservation dans la BDD en fonction des paramètres choisis dans le formulaire de la page reservation
def resDone(request, lieu_id, user_id, platP_id):
    date = datetime.now()
    plat = PlatPrincipal.objects.get(pk=platP_id)
    res = Reservation(prix = plat.prix, date = date, user_id=user_id, lieu_id = lieu_id)
    res.save()
    return redirect('profil', user_id = user_id)