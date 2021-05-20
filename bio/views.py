from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import About, Assisted, Shows, Editorials, Celebrities, Music, Tv, Commercials

from .forms import AboutForm, AssistedForm, ShowsForm, EditorialsForm, CelebritiesForm, MusicForm, TvForm, CommercialsForm


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


@login_required
def edit_shows(request, shows_id):
    """ Edit shows section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('bio'))

    shows_section = get_object_or_404(Shows, pk=shows_id)
    # shows social icons in a footer
    
    if request.method == 'POST':
        shows_form = ShowsForm(request.POST, instance=shows_section)
        if shows_form.is_valid():
            shows_form.save()
            messages.success(request, 'Section edited successfully!')
            return redirect(reverse('bio'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        shows_form = ShowsForm(instance=shows_section)
        messages.info(request, 'You are editing shows section!')

    template = 'bio/includes/edit-templates/edit-shows.html'
    context = {
        'shows_form': shows_form,
        'shows_section': shows_section,
    }

    return render(request, template, context)


@login_required
def edit_editorials(request, editorials_id):
    """ Edit editorials section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('bio'))

    editorials_section = get_object_or_404(Editorials, pk=editorials_id)
    # editorials social icons in a footer
    
    if request.method == 'POST':
        editorials_form = EditorialsForm(request.POST, instance=editorials_section)
        if editorials_form.is_valid():
            editorials_form.save()
            messages.success(request, 'Section edited successfully!')
            return redirect(reverse('bio'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        editorials_form = EditorialsForm(instance=editorials_section)
        messages.info(request, 'You are editing editorials section!')

    template = 'bio/includes/edit-templates/edit-editorials.html'
    context = {
        'editorials_form': editorials_form,
        'editorials_section': editorials_section,
    }

    return render(request, template, context)


@login_required
def edit_celebrities(request, celebrities_id):
    """ Edit celebrities section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('bio'))

    celebrities_section = get_object_or_404(Celebrities, pk=celebrities_id)
    # celebrities social icons in a footer
    
    if request.method == 'POST':
        celebrities_form = CelebritiesForm(request.POST, instance=celebrities_section)
        if celebrities_form.is_valid():
            celebrities_form.save()
            messages.success(request, 'Section edited successfully!')
            return redirect(reverse('bio'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        celebrities_form = CelebritiesForm(instance=celebrities_section)
        messages.info(request, 'You are editing celebrities section!')

    template = 'bio/includes/edit-templates/edit-celebrities.html'
    context = {
        'celebrities_form': celebrities_form,
        'celebrities_section': celebrities_section,
    }

    return render(request, template, context)


@login_required
def edit_music(request, music_id):
    """ Edit music section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('bio'))

    music_section = get_object_or_404(Music, pk=music_id)
    # music social icons in a footer
    
    if request.method == 'POST':
        music_form = MusicForm(request.POST, instance=music_section)
        if music_form.is_valid():
            music_form.save()
            messages.success(request, 'Section edited successfully!')
            return redirect(reverse('bio'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        music_form = MusicForm(instance=music_section)
        messages.info(request, 'You are editing music section!')

    template = 'bio/includes/edit-templates/edit-music.html'
    context = {
        'music_form': music_form,
        'music_section': music_section,
    }

    return render(request, template, context)


@login_required
def edit_tv(request, tv_id):
    """ Edit tv section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('bio'))

    tv_section = get_object_or_404(Tv, pk=tv_id)
    # tv social icons in a footer
    
    if request.method == 'POST':
        tv_form = TvForm(request.POST, instance=tv_section)
        if tv_form.is_valid():
            tv_form.save()
            messages.success(request, 'Section edited successfully!')
            return redirect(reverse('bio'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        tv_form = TvForm(instance=tv_section)
        messages.info(request, 'You are editing tv section!')

    template = 'bio/includes/edit-templates/edit-tv.html'
    context = {
        'tv_form': tv_form,
        'tv_section': tv_section,
    }

    return render(request, template, context)


@login_required
def edit_commercials(request, commercials_id):
    """ Edit commercials section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('bio'))

    commercials_section = get_object_or_404(Commercials, pk=commercials_id)
    # commercials social icons in a footer
    
    if request.method == 'POST':
        commercials_form = CommercialsForm(request.POST, instance=commercials_section)
        if commercials_form.is_valid():
            commercials_form.save()
            messages.success(request, 'Section edited successfully!')
            return redirect(reverse('bio'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        commercials_form = CommercialsForm(instance=commercials_section)
        messages.info(request, 'You are editing commercials section!')

    template = 'bio/includes/edit-templates/edit-commercials.html'
    context = {
        'commercials_form': commercials_form,
        'commercials_section': commercials_section,
    }

    return render(request, template, context)