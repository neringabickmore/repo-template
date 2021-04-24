from django import forms


class ContactForm(forms.Form):
    """
    Contact form page
    """

    full_name = forms.CharField(
         label="Full Name"
    )
    email = forms.EmailField(
        label="Email"
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "rows": 6,
            "maxlength": 500,
            "placeholder": '500 characters max',
        })
    )

    class Meta:
        fields = ['full_name', 'email', 'message']