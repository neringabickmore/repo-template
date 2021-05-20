from django.urls import path
from . import views

urlpatterns = [
    path('', views.bio, name='bio'),
    path('edit/about/<int:about_id>/', views.edit_about, name='edit_about'),
    path('edit/assisted/<int:assisted_id>/', views.edit_assisted, name='edit_assisted'),
    path('edit/shows/<int:shows_id>/', views.edit_shows, name='edit_shows'),
    path('edit/editorials/<int:editorials_id>/', views.edit_editorials, name='edit_editorials'),
]