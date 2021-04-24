from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse

from .forms import ContactForm


def contact(request):
    """ A view to return contact page """

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            user_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    # captures user email in subject field
                    f"Message from {full_name}, <{user_email}>",
                    message,
                    user_email,
                    [settings.O365_EMAIL],
                    fail_silently=False
                )
                return redirect('message_sent')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


def message_sent(request):
    """
    A view to return message-sent page to let the user know\
    the message was sent.
    """
    return render(request, 'contact/message-sent.html')