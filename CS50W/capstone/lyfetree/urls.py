"""
URL configuration for lyfetree project.

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

from journey import views as journey_views
from account import views as account_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", journey_views.index_view, name="index"),
        path("login/", account_views.login_view, name="login"),
    path("register/", account_views.register_view, name="register"),
    path("logout/", account_views.logout_view, name="logout"),
    path("journey/", journey_views.journey_view, name="journey"),
    path('create_milestone/', journey_views.create_milestone, name='create_milestone'),
]
