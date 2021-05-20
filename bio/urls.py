from django.urls import path
from . import views

urlpatterns = [
    path('', views.bio, name='bio'),
    path('edit/about/<int:about_id>/', views.edit_about, name='edit_about'),
    path('edit/assisted/<int:assisted_id>/', views.edit_assisted, name='edit_assisted'),
    path('edit/shows/<int:shows_id>/', views.edit_shows, name='edit_shows'),
    path('edit/editorials/<int:editorials_id>/', views.edit_editorials, name='edit_editorials'),
    path('edit/celebrities/<int:celebrities_id>/', views.edit_celebrities, name='edit_celebrities'),
    path('edit/music/<int:music_id>/', views.edit_music, name='edit_music'),
    path('edit/tv/<int:tv_id>/', views.edit_tv, name='edit_tv'),
    path('edit/commercials/<int:commercials_id>/', views.edit_commercials, name='edit_commercials'),
]