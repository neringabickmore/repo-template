from django import forms
from .widgets import CustomClearableFileInput
from .models import Photo

class PhotoForm (forms.ModelForm):

    class Meta:
        model = Photo
        fields = '__all__'
    
    image = forms.ImageField(
        label='Image', required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
        labels = {
            'title': 'Title with no spaces',
            'friendly_title': 'Display title',
            'image': 'Upload photo',
        }
        for field in self.fields:
            self.fields[field].label = labels[field]
            self.fields['title'].widget.attrs['class'] = 'field-styling'
            self.fields['friendly_title'].widget.attrs['class'] = 'field-styling'
            self.fields['image'].widget.attrs['class'] = 'field-styling'
            self.fields['title'].widget.attrs['data-toggle'] = 'tooltip'
            self.fields['title'].widget.attrs['data-placement'] = 'top'
            self.fields['title'].widget.attrs['title'] = 'No spaces \
                or special characters, use - for word separation'