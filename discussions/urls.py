from django.urls import path
from .views import discussions, toggle_like


urlpatterns = [
    path('discussions/', discussions, name='discussions'),
    path('discussions/<int:pk>/likes', toggle_like, name='toggle_like'),
]
