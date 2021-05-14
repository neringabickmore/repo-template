from django.contrib import admin
from .models import About, Assisted, Shows, Editorials, Celebrities, Music, Tv, Commercials

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


class EditorialsAdmin(admin.ModelAdmin):
    """
    Editorials section admin
    """

    list_display = (
        'name',
        'description',
    )


class CelebritiesAdmin(admin.ModelAdmin):
    """
    Celebrities section admin
    """

    list_display = (
        'name',
        'description',
    )


class MusicAdmin(admin.ModelAdmin):
    """
    Music section admin
    """

    list_display = (
        'name',
        'description',
    )

class TvAdmin(admin.ModelAdmin):
    """
    TV section admin
    """

    list_display = (
        'name',
        'description',
    )

class CommercialsAdmin(admin.ModelAdmin):
    """
    Commercials section admin
    """

    list_display = (
        'name',
        'description',
    )   

admin.site.register(Commercials, CommercialsAdmin)
admin.site.register(Tv, TvAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Celebrities, CelebritiesAdmin)
admin.site.register(Editorials, EditorialsAdmin)
admin.site.register(Shows, ShowsAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Assisted, AssistedAdmin)