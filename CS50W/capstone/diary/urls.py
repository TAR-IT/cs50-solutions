"""
URL configuration for diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from entries import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.index_view, name="index"),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('favourize_entry/<int:entry_id>/', views.favourize_entry, name='favourize_entry'),
    path('add_comment/<int:entry_id>/', views.add_comment, name='add_comment'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]
