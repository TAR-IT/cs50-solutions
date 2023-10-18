from django import forms
from .models import AuctionListing, Bid, Comment, Category

class CreateListingForm(forms.ModelForm):
    image_url = forms.URLField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'start_bid', 'image_url', 'category']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']