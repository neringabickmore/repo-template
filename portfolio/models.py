from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Photo (models.Model):

    """
    Model for Photos.
    """
    class Meta:
        verbose_name_plural = "Photos"

    title = models.CharField("Title", max_length=200)
    friendly_title = models.CharField("Friendly Title", max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to= 'media/', blank=False)

    sort = ('date_time')

    def __str__(self):
        return self.title

    def get_friendly_name(self):
        return self.friendly_title