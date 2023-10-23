from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
import json

from .models import User, DiaryEntry, EntryComment
from .forms import EntryCommentForm

def index_view(request):
    # Add any context data you want to pass to the template here
    if request.method == "POST":
        if "comment_content" in request.POST:
            # Create a new comment
            comment_content = request.POST["comment_content"]
            if comment_content:
                entry_id = request.POST.get("entry_id")
                try:
                    entry = DiaryEntry.objects.get(pk=entry_id)
                    comment = EntryComment(entry=entry, content=comment_content, user=request.user)
                    comment.save()
                except DiaryEntry.DoesNotExist:
                    pass
        elif "content" in request.POST:
            # Create a new post
            content = request.POST["content"]
            if content:
                entry = DiaryEntry(user=request.user, content=content)
                entry.save()

    # Retrieve all posts and paginate them
    entries = DiaryEntry.objects.all().order_by("-created_at")
    paginator = Paginator(entries, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Add an "Edit" button for posts created by the current user
    for entry in page_obj:
        entry.editable = entry.user == request.user

    # Check which posts have been favorited by the current user
    favourized_entries = set(request.user.favourized_entries.all().values_list('id', flat=True))

    # Pass the favorited entries to the template
    return render(request, "index.html", {
        "page_obj": page_obj,
        "favourized_entries": favourized_entries,
    })

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("diary"))
    else:
        return render(request, "register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("diary"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def edit_entry(request, entry_id):
    # Retrieve the JSON data sent by JavaScript
    data = json.loads(request.body.decode('utf-8'))
    edited_content = data.get('content', '')

    try:
        entry = DiaryEntry.objects.get(pk=entry_id, user=request.user)
        entry.content = edited_content
        entry.save()
        
        return JsonResponse({'success': True, 'content': entry.content})
    except DiaryEntry.DoesNotExist:
        return JsonResponse({'success': False, 'error_message': 'Post not found or not owned by the user'})

@login_required
def add_comment(request, entry_id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        comment_content = data.get('comment_content', '')


        try:
            entry = DiaryEntry.objects.get(pk=entry_id)
            comment = EntryComment(entry=entry, content=comment_content, user=request.user)
            comment.save()

            # Return a JSON response indicating success
            return JsonResponse({'success': True})
        except DiaryEntry.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Entry not found'})
    else:
        return JsonResponse({'success': False, 'error_message': 'Invalid request method'})

@login_required
def favourize_entry(request, entry_id):
    if request.method == "POST":
        entry = get_object_or_404(DiaryEntry, id=entry_id)
        user = request.user

        if entry.favourized.filter(id=user.id).exists():
            # User already liked the post, so unlike it
            entry.favourized.remove(user)
            favourized = False
        else:
            # User hasn't liked the post yet, so like it
            entry.favourized.add(user)
            favourized = True

        return JsonResponse({'success': True, 'favourized': favourized})

    return JsonResponse({'success': False, 'error_message': 'Invalid request method'})

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, pk=entry_id)

    # Check if the request user is the owner of the post
    if entry.user == request.user:
        entry.delete()
    
    return redirect('index')  # Redirect to the main page after deleting