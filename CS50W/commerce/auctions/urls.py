from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('listing/<int:listing_id>/close_auction/', views.close_auction, name='close_auction'),
    path('listing/<int:listing_id>/', views.listing, name='listing'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>/', views.category_listings, name='category_listings'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('listing/<int:listing_id>/add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('admin/', admin.site.urls),
]
