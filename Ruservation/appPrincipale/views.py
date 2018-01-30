from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Ruservation.forms import SignUpForm, ParamForm
from appPrincipale.models import LieuRestauration, Menu, MenuPlatPrincipal, PlatPrincipal, UserProfile, Favoris, Regime, Allergie
# Create your views here.
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

def home(request):
    lieux = LieuRestauration.objects.all()
    fav = Favoris.objects.all()
    return render(request, 'appPrincipale/home.html', {'lieux': lieux, 'fav' : fav})

def lieuR(request, lieu_id):
    lieu = LieuRestauration.objects.get(pk=lieu_id)
    menu = get_object_or_404(Menu, lieuRestauration_id = lieu.id)
    menupp = MenuPlatPrincipal.objects.filter(menu_id = menu.id)
    platPrincipal = PlatPrincipal.objects.all()
    return render(request, 'appPrincipale/lieu.html', {'lieu': lieu, 'menu': menu, 'plats': platPrincipal, 'menupp': menupp})

def profil(request, user_id):
    if UserProfile.objects.filter(user_id=user_id).count() == 0:
        userProfil = UserProfile(ville='Nancy', lieuEtude='ARTEM', solde=0, user_id=user_id)
        userProfil.save()
    else:
        userProfil = UserProfile.objects.get(user_id=user_id)
        regimes = Regime.objects.get(pk=userProfil.regime_id)
        allergies = Allergie.objects.get(pk=userProfil.allergie_id)
    return render(request, 'appPrincipale/profil.html', {'userProfil': userProfil, 're' : regimes, 'al' : allergies})

def addFav(request, lieu_id, user_id):
    userP = UserProfile.objects.get(user_id=user_id)
    if Favoris.objects.filter(user_id=user_id, lieu_id=lieu_id).count()>0:
        Favoris.objects.filter(user_id=user_id, lieu_id=lieu_id).delete()
    else:
        f = Favoris(user_id=user_id, lieu_id=lieu_id)
        f.save()
    fav = Favoris.objects.filter(user_id=user_id).values_list('lieu_id', flat='True')
    lieux = LieuRestauration.objects.filter(id__in = fav)
    return render(request, 'appPrincipale/favoris.html', {'lieux' : lieux, 'userP' : userP})

def favoris(request, user_id):
    userP = UserProfile.objects.get(user_id=user_id)
    fav = Favoris.objects.filter(user_id=user_id).values_list('lieu_id', flat='True')
    lieux = LieuRestauration.objects.filter(id__in = fav)
    return render(request, 'appPrincipale/favoris.html', {'lieux' : lieux, 'userP' : userP})

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

def get_Param(request, user_id):
    form = ParamForm(request.POST)
    if form.is_valid():
        userP = UserProfile.objects.get(user_id=user_id)
        al = Allergie.objects.get(pk=userP.allergie_id)
        re = Regime.objects.get(pk=userP.regime_id)

        userP.ville = form.cleaned_data['ville']
        userP.lieuEtude = form.cleaned_data['etab']
        al.sGluten = form.cleaned_data['sGluten']
        al.sLactose = form.cleaned_data['sLactose']
        re.vegetarien = form.cleaned_data['vegetarien']
        re.vegan = form.cleaned_data['vegan']
        
        userP.save()
        al.save()
        re.save()

    return render(request, 'appPrincipale/parametres.html', {'userP': userP, 're' : re, 'al' : al})

def geoLoc(request, lieu_id):
    lieu = LieuRestauration.objects.get(pk=lieu_id)

    return render(request, 'appPrincipale/geoLoc.html', {'lieu': lieu})