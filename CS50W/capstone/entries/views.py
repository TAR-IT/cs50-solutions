from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import DiaryEntry

def index_view(request):
    # Add any context data you want to pass to the template here
    context = {
        'welcome_message': 'Welcome to the Diary App!',
    }
    return render(request, 'index.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('diary')  # Redirect to a user's dashboard or profile page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('diary')  # Redirect to a user's dashboard or profile page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('diary')  # Redirect to the login page after logout

def diary_view(request):
    entries = DiaryEntry.objects.all()
    context = {'entries': entries}
    return render(request, 'diary.html', context)

def create_entry(request):
    if request.method == 'POST':
        # Process the form data and create the new diary entry
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        tags = request.POST.get('tags')

        # Create the DiaryEntry instance and save it
        entry = DiaryEntry(user=request.user, title=title, category=category, description=description, tags=tags)
        entry.save()

        # Respond with JSON data, you can include the newly created entry data
        return JsonResponse({'message': 'Entry created successfully'})

