from django.shortcuts import render

from .models import Site


def index_view(request):
    details = Site.objects.all()

    context = {
        "title": "Home",
        "details": details,
    }

    return render(request, "webapp/index.html", context)


def about_view(request):
    context = {
        "title": "About"
    }

    return render(request, "webapp/about.html", context)


def contacts_view(request):
    context = {
        "title": "Contacts"
    }

    return render(request, "webapp/contacts.html", context)
