from django.shortcuts import render

from .models import Site


def index_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Webapp/index.html", context)


def about_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Webapp/about.html", context)


