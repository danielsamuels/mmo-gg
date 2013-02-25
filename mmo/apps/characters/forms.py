from django.core.urlresolvers import reverse_lazy
from django import forms
from models import Character

class CharacterCreateForm(forms.ModelForm):

    class Meta:
        model = Character
        exclude = ("user", "xp", "level")
