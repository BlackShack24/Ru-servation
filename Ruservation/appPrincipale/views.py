from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Ruservation.forms import SignUpForm
from appPrincipale.models import LieuRestauration, Menu, MenuPlatPrincipal, PlatPrincipal, UserProfile
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
    return render(request, 'appPrincipale/home.html', {'lieux': lieux})

def lieuR(request, lieu_id):
    lieu = LieuRestauration.objects.get(pk=lieu_id)
    menu = get_object_or_404(Menu, lieuRestauration_id = lieu.id)
    menupp = MenuPlatPrincipal.objects.filter(menu_id = menu.id)
    platPrincipal = PlatPrincipal.objects.all()
    return render(request, 'appPrincipale/lieu.html', {'lieu': lieu, 'menu': menu, 'plats': platPrincipal, 'menupp': menupp})

def profil(request, user_id):
	userProfil = UserProfile.objects.get(user_id=user_id)
	return render(request, 'appPrincipale/profil.html', {'userProfil': userProfil})