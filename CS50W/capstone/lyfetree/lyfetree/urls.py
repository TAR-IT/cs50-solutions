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
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import admin
from django.urls import path
from journey import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.custom_register, name='register'),
    # Create Milestone
    path('create_milestone/', views.create_milestone, name='create_milestone'),

    # Edit Milestone
    path('edit_milestone/<int:milestone_id>/', views.edit_milestone, name='edit_milestone'),

    # Rename Milestone
    path('rename_milestone/<int:milestone_id>/', views.rename_milestone, name='rename_milestone'),

    # Change Milestone Description
    path('change_milestone_description/<int:milestone_id>/', views.change_milestone_description, name='change_milestone_description'),
    path('', views.index, name='index'),
]
