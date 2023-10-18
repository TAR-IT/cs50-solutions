from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Milestone
from .forms import MilestoneCreateForm, MilestoneRenameForm, MilestoneCreateForm, MilestoneChangeForm

@login_required
def index(request):
    user = request.user
    milestones = Milestone.objects.filter(user=user)
    
    context = {
        'milestones': milestones,
    }
    
    return render(request, 'index.html', context)

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Replace with your desired success URL
    else:
        form = AuthenticationForm(request)
    return render(request, 'registration/login.html', {'form': form})

def custom_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Replace with your desired success URL
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_milestone(request):
    if request.method == 'POST':
        form = MilestoneCreateForm(request.POST)
        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.user = request.user
            milestone.save()
            return redirect('index')
    else:
        form = MilestoneCreateForm()
    
    return render(request, 'create_milestone.html', {'form': form})

def rename_milestone(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id, user=request.user)
    
    if request.method == 'POST':
        form = MilestoneRenameForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MilestoneRenameForm(instance=milestone)
    
    return render(request, 'rename_milestone.html', {'form': form, 'milestone': milestone})

def change_milestone_description(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id, user=request.user)
    
    if request.method == 'POST':
        form = MilestoneChangeForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MilestoneChangeForm(instance=milestone)
    
    return render(request, 'change_milestone_description.html', {'form': form, 'milestone': milestone})

def edit_milestone(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id, user=request.user)
    
    if request.method == 'POST':
        form = MilestoneRenameForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MilestoneRenameForm(instance=milestone)
    
    return render(request, 'edit_milestone.html', {'form': form, 'milestone': milestone})