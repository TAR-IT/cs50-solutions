from django.shortcuts import render, redirect
from django import forms

from . import util
import random
import markdown2


def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry_page(request, title):
    entry_content = util.get_entry(title)

    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "error_message": "Page not found"
        })

    entry_html = markdown2.markdown(entry_content)

    return render(request, "encyclopedia/entry_page.html", {
        "title": title,
        "content": entry_html
    })

def search_page(request):
    query = request.GET.get('q', '')
    entries = util.list_entries()

    matching_entries = [entry for entry in entries if query.lower() in entry.lower()]

    if util.get_entry(query):
        return redirect('entry_page', title=query)
    else:
        return render(request, "encyclopedia/search_results.html", {
            "query": query,
            "matching_entries": matching_entries
        })

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea)

def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if util.get_entry(title):
                return render(request, "encyclopedia/error.html", {
                    "error_message": "Entry already exists"
                })

            util.save_entry(title, content)
            return redirect('entry_page', title=title)
    else:
        form = NewPageForm()

    return render(request, "encyclopedia/new_page.html", {
        "form": form
    })

class EditPageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="Content (Markdown)")

def edit_page(request, title):
    entry_content = util.get_entry(title)

    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "error_message": "Page not found"
        })

    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            new_content = form.cleaned_data["content"]
            util.save_entry(title, new_content)
            return redirect('entry_page', title=title)
    else:
        form = EditPageForm(initial={"content": entry_content})

    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "form": form
    })

def random_page(request):
    entries = util.list_entries()
    if entries:
        random_entry = random.choice(entries)
        return redirect('entry_page', title=random_entry)
    else:
        return render(request, "encyclopedia/error.html", {
            "error_message": "No entries available"
        })