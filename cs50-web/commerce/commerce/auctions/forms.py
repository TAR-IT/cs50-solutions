from django import forms
from .models import AuctionListing, Bid, Comment, Category

class CreateListingForm(forms.ModelForm):
    image_url = forms.URLField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    class Meta:
        model = AuctionListing
        fields = ['title', 'description', 'start_bid', 'image_url', 'category']

class BidForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is None:
            raise forms.ValidationError("Bid amount is required.")
        else:
            bid_form = BidForm()
        return amount

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']