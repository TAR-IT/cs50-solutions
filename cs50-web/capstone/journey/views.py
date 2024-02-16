from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from .models import Milestone

def index_view(request):
    return render(request, 'index.html')

@login_required
def journey_view(request):
    user = request.user  # Get the current logged-in user
    
    # Query the Milestone model to get user-specific data
    user_milestones = Milestone.objects.filter(user=user)
    
    context = {
        'user_milestones': user_milestones,  # Pass the data to the template
    }
    return render(request, 'journey.html', context)

@login_required
def create_milestone(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')

        if title and content:
            # Create a new entry and save it to the database
            milestone = Milestone(user=request.user, title=title, content=content)
            milestone.save()
            return JsonResponse({'success': True, 'title': milestone.title, 'content': milestone.content})
        else:
            return JsonResponse({'success': False, 'error_message': 'Title and content are required.'})

