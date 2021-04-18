from django.shortcuts import render


def bio(request):
    """ A view to return bio page """

    return render(request, 'bio/bio.html')
