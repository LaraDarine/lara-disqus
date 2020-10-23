from django.urls import path
from .views import discussions, toggle_like, toggle_dislike


urlpatterns = [
    path('discussions/', discussions, name='discussions'),
    path('discussions/<int:pk>/likes', toggle_like, name='toggle_like'),
    path('discussions/<int:pk>/dislikes', toggle_dislike, name='toggle_dislike'),
]
