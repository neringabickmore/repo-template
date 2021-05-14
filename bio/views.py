from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import About, Assisted, Shows


def bio(request):
    """ A view to return bio page """

    about_section = About.objects.all()
    assisted_section = Assisted.objects.all()
    shows_section = Shows.objects.all()

    template = 'bio/bio.html'
    context = {
        'about_section': about_section,
        'assisted_section': assisted_section,
        'shows_section': shows_section,
    }

    return render(request, template, context)
