from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import About, Assisted, Shows, Editorials, Celebrities, Music, Tv, Commercials


def bio(request):
    """ A view to return bio page """

    about_section = About.objects.all()
    assisted_section = Assisted.objects.all()
    shows_section = Shows.objects.all()
    editorials_section = Editorials.objects.all()
    celebrities_section = Celebrities.objects.all()
    music_section = Music.objects.all()
    tv_section = Tv.objects.all()
    commercials_section = Commercials.objects.all()

    template = 'bio/bio.html'
    context = {
        'about_section': about_section,
        'assisted_section': assisted_section,
        'shows_section': shows_section,
        'editorials_section': editorials_section,
        'celebrities_section': celebrities_section, 
        'music_section': music_section,
        'tv_section': tv_section,
        'commercials_section': commercials_section,

    }

    return render(request, template, context)
