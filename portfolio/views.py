from django.shortcuts import render


def portfolio(request):
    """ A view to show all portfolio items"""

    return render(request, 'portfolio/portfolio.html')
