from django import forms
from .models import About, Assisted, Shows, Editorials, Celebrities, Music, Tv, Commercials


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


class ShowsForm(forms.ModelForm):
    """
    Shows form on the home page
    """

    class Meta:
        model = Shows
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


class EditorialsForm(forms.ModelForm):
    """
    Editorials form on the home page
    """

    class Meta:
        model = Editorials
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


class CelebritiesForm(forms.ModelForm):
    """
    Celebrities form on the home page
    """

    class Meta:
        model = Celebrities
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


class MusicForm(forms.ModelForm):
    """
    Music form on the home page
    """

    class Meta:
        model = Music
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


class TvForm(forms.ModelForm):
    """
    Tv form on the home page
    """

    class Meta:
        model = Tv
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


class CommercialsForm(forms.ModelForm):
    """
    Commercials form on the home page
    """

    class Meta:
        model = Commercials
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