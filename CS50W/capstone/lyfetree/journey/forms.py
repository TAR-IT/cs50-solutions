from django import forms
from .models import Milestone

class MilestoneCreateForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['title', 'description']

class MilestoneRenameForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['title']

class MilestoneChangeForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['description']