from django import forms
from .models import About, Assisted


class AboutForm(forms.ModelForm):
    """
    About form on the home page
    """

    class Meta:
        model = About
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Section title',
            'description': 'Description',
        }
        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['name'].widget.attrs['class'] = 'field-styling'
        self.fields['description'].widget.attrs['class'] = 'field-styling'


class AssistedForm(forms.ModelForm):
    """
    Assisted form on the home page
    """

    class Meta:
        model = Assisted
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Section title',
            'description': 'Description',
        }
        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['name'].widget.attrs['class'] = 'field-styling'
        self.fields['description'].widget.attrs['class'] = 'field-styling'