from django.contrib import admin
from .models import About, Assisted

class AboutAdmin(admin.ModelAdmin):
    """
    About section admin
    """

    list_display = (
        'name',
        'description',
    )

class AssistedAdmin(admin.ModelAdmin):
    """
    Assisted section admin
    """

    list_display = (
        'name',
        'description',
    )

admin.site.register(About, AboutAdmin)
admin.site.register(Assisted, AssistedAdmin)