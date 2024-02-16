from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import CreateListingForm, BidForm, CommentForm
from .models import User, AuctionListing, Bid, Comment, Category, Watchlist


def index(request):
    listings = AuctionListing.objects.filter(active=True)
    return render(request, 'auctions/index.html', {'listings': listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CreateListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            return redirect('index')
    else:
        form = CreateListingForm()
    return render(request, 'auctions/create_listing.html', {'form': form, 'categories': categories})

def active_listings(request):
    active_listings = AuctionListing.objects.filter(active=True)
    return render(request, 'auctions/active_listings.html', {'active_listings': active_listings})

def listing(request, listing_id):
    listing = get_object_or_404(AuctionListing, id=listing_id, active=True)
    comments = Comment.objects.filter(listing=listing)

    bid_form = BidForm(request.POST or None)  # Initialize BidForm with POST data

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.listing = listing
            new_comment.commenter = request.user
            new_comment.save()
            return redirect('listing', listing_id=listing_id)
    else:
        comment_form = CommentForm()

    if request.method == 'POST':
        if bid_form.is_valid():
            bid_amount = bid_form.cleaned_data['amount']
            if bid_amount >= listing.start_bid and bid_amount > listing.current_bid:
                new_bid = Bid(listing=listing, bidder=request.user, amount=bid_amount)
                new_bid.save()
                listing.current_bid = bid_amount
                listing.save()
                messages.success(request, 'Your bid was placed successfully!')
            else:
                messages.error(request, 'Invalid bid amount. Please enter a valid amount.')

        if request.user == listing.seller and not listing.is_closed:
            listing.is_closed = True
            highest_bid = Bid.objects.filter(listing=listing).order_by('-amount').first()
            if highest_bid:
                listing.winner = highest_bid.bidder
                listing.save()
                messages.success(request, 'The auction has been closed. The winner is the highest bidder.')
            else:
                messages.error(request, 'The auction cannot be closed without any bids.')

    return render(request, 'auctions/listing.html', {'listing': listing, 'comments': comments, 'comment_form': comment_form, 'bid_form': bid_form})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'auctions/categories.html', {'categories': categories})

def category_listings(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    listings = AuctionListing.objects.filter(category=category, active=True)
    return render(request, 'auctions/category_listings.html', {'category': category, 'listings': listings})

@login_required
def watchlist(request):
    user_watchlist = Watchlist.objects.filter(user=request.user).first()
    return render(request, 'auctions/watchlist.html', {'watchlist': user_watchlist})

@login_required
def add_to_watchlist(request, listing_id):
    listing = get_object_or_404(AuctionListing, pk=listing_id)
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    watchlist.listings.add(listing)
    return redirect('listing', listing_id=listing.id)

@login_required
def remove_from_watchlist(request, listing_id):
    listing = get_object_or_404(AuctionListing, pk=listing_id)
    watchlist = Watchlist.objects.filter(user=request.user).first()
    if watchlist:
        watchlist.listings.remove(listing)
    return redirect('listing', listing_id=listing.id)

@login_required
def close_auction(request, listing_id):
    listing = get_object_or_404(AuctionListing, pk=listing_id, seller=request.user)

    if listing.active:
        # Set the auction as closed
        listing.active = False
        listing.save()

        # Determine the winner (highest bidder)
        highest_bid = listing.bids.order_by('-amount').first()
        if highest_bid:
            listing.winner = highest_bid.bidder
            listing.save()

    return redirect('listing', listing_id=listing_id)