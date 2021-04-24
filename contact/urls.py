from django.urls import path
from . import views

urlpatterns = [
    path(
        '', views.contact,
        name='contact'),
    path(
        'message-sent/', views.message_sent,
        name='message_sent'),
]
