from django import forms
from .models import EntryComment

class EntryCommentForm(forms.ModelForm):
    class Meta:
        model = EntryComment  # Specify the Comment model
        fields = ['content', 'entry']  # Define the fields you want to include in the form
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Add a comment...'}),
    )