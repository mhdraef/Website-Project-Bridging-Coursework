from django import forms

from .models import *

class EduForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('university', 'course','location','graduation','description')

class ProjForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'type','languages','repository','description')

class ExpForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('position', 'company','location','date','description')

class CertForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = ('name', 'date', 'company')


class SkiForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ('topic', 'skill')
