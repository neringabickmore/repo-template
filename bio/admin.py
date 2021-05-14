from django.contrib import admin
from .models import About, Assisted, Shows

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


class ShowsAdmin(admin.ModelAdmin):
    """
    Assisted section admin
    """

    list_display = (
        'name',
        'description',
    )

admin.site.register(Shows, ShowsAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Assisted, AssistedAdmin)