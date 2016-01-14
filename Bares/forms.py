# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from Bares.models import Bar, Tapa, UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

        
class BarForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="El nombre de su establecimiento.", label="Nombre")
    lema = forms.CharField(max_length=140, help_text = "Su lema en 140 caracteres")
    descripcion = forms.CharField(widget=forms.Textarea, help_text="Defina su establecimiento")
    direccion = forms.CharField(help_text = "Dirección de su establecimiento")
    visitas = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    precio_refresco = forms.DecimalField(initial = 0.0, max_digits=2, decimal_places=1, help_text="Refresco (€)")
    precio_cerveza = forms.DecimalField(initial = 0.0, max_digits=2, decimal_places=1, help_text="Cerveza (€)")
    precio_cubata = forms.DecimalField(initial = 0.0, max_digits=2, decimal_places=1, help_text="Cubata (€)")
    logo = forms.ImageField(help_text='Un logo para su establecimiento')
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bar
        fields = ('nombre','lema','descripcion','direccion','visitas','precio_refresco', 'precio_cerveza','precio_cubata', 'logo')


class TapaForm(forms.ModelForm):
    titulo = forms.CharField(max_length=128, help_text="Insertar el título de la tapa.")
    descripcion = forms.CharField(widget=forms.Textarea, help_text="Insertar la descripción de la tapa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapa
        
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('bar',)
        #or specify the fields to include (i.e. not include the category field)
        fields = ('titulo', 'descripcion')