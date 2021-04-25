from django.urls import path
from . import views

urlpatterns = [
    path(
        '', views.portfolio,
        name='portfolio'),
    path(
        'upload/photo', views.upload_photo,
        name='upload_photo'),
]
