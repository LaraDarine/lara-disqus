from django.urls import path
from .views import discussions

urlpatterns = [
    path('discussions/', discussions, name='discussions'),
]