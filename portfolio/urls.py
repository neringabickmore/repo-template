from django.urls import path
from . import views

urlpatterns = [
    path(
        '', views.portfolio,
        name='portfolio'),
    path(
        'upload/photo', views.upload_photo,
        name='upload_photo'),
    path(
        'delete/photo/<int:photo_id>/', views.delete_photo,
        name='delete_photo')
]
