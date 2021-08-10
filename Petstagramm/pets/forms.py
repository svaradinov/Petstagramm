from django import forms

from Petstagramm.core.forms import BootstrapFormMixin
from Petstagramm.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

