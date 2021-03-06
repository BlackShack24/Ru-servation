from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ParamForm(forms.Form):
    vegetarien = forms.BooleanField(required=False)
    vegan = forms.BooleanField(required=False)
    sGluten = forms.BooleanField(required=False)
    sLactose = forms.BooleanField(required=False)
    ville = forms.CharField(max_length=30, required=False)
    etab = forms.CharField(max_length=30, required=False)