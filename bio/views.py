from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import About, Assisted, Shows, Editorials, Celebrities, Music, Tv, Commercials

from .forms import AboutForm, AssistedForm


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


@login_required
def edit_about(request, about_id):
    """ Edit about section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('bio'))

    about_section = get_object_or_404(About, pk=about_id)
    # shows social icons in a footer
    
    if request.method == 'POST':
        about_form = AboutForm(request.POST, instance=about_section)
        if about_form.is_valid():
            about_form.save()
            messages.success(request, 'Section edited successfully!')
            return redirect(reverse('bio'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        about_form = AboutForm(instance=about_section)
        messages.info(request, 'You are editing about section!')

    template = 'bio/includes/edit-templates/edit-about.html'
    context = {
        'about_form': about_form,
        'about_section': about_section,
    }

    return render(request, template, context)


@login_required
def edit_assisted(request, assisted_id):
    """ Edit assisted section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('bio'))

    assisted_section = get_object_or_404(Assisted, pk=assisted_id)
    # shows social icons in a footer
    
    if request.method == 'POST':
        assisted_form = AssistedForm(request.POST, instance=assisted_section)
        if assisted_form.is_valid():
            assisted_form.save()
            messages.success(request, 'Section edited successfully!')
            return redirect(reverse('bio'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        assisted_form = AssistedForm(instance=assisted_section)
        messages.info(request, 'You are editing assisted section!')

    template = 'bio/includes/edit-templates/edit-assisted.html'
    context = {
        'assisted_form': assisted_form,
        'assisted_section': assisted_section,
    }

    return render(request, template, context)