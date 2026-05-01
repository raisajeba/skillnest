from django import forms
from django.forms import inlineformset_factory
from .models import Skill, SkillImage

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['category', 'name', 'description', 'skill_level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'skill_level': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


SkillImageFormSet = inlineformset_factory(
    Skill,
    SkillImage,
    fields=['image'],
    extra=1
)