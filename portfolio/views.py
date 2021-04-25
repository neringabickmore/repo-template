from django.shortcuts import render, redirect
from django.contrib import messages

import cloudinary
import cloudinary.uploader
import cloudinary.api

from .models import Photo
from .forms import PhotoForm

from cloudinary.forms import cl_init_js_callbacks

def portfolio(request):
    """ A view to show all portfolio items"""
    photos = Photo.objects.all().order_by('-date_time')

    context = {
        'photos': photos
    }
    path = 'portfolio/portfolio.html'

    return render(request, path, context)


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect('portfolio')
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.') 

    else:
        form = PhotoForm()

    context = {
        'form': form
    }
    return render(request, 'portfolio/upload-photo.html', context)