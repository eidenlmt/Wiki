from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": util.get_entry(title)
    })

def title(request, title):
    f = open(f"entries/{title}.md", "r")
    return render(request, "encyclopedia/entry.html", {
        "htmltitle": f.readline()
    })