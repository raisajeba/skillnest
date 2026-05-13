from django import forms
from .models import Profile
from skills.models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description','image','category']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'image']