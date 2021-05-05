from django.contrib import admin

from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    """
    Photo management in admin.
    """

    list_display = (
        'friendly_title',
        'date_time',
    )

    ordering = ('date_time',)

# Register your models here.
admin.site.register(Photo, PhotoAdmin)