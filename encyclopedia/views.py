from django.shortcuts import render
from django import forms
from . import util

class SearchQueue(forms.Form):
    q = forms.CharField(label="New Task")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": util.get_entry(title)
    })

def add(request):
    if request.method == 'POST':
        form = SearchQueue(request.POST)
        if form.is_valid():
            q = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "task/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

#not working
#def title(request, title):
#    f = open(f"entries/{title}.md", "r")
#    return render(request, "encyclopedia/entry.html", {
#        "htmltitle": f.readline()
#    })