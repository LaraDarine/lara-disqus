from django.urls import path
from .views import discussions, discussion_details, toggle_like, toggle_dislike, home, delete_comment


urlpatterns = [
    path('discussions/welcome', home, name='home'),
    path('discussions/', discussions, name='discussions'),
    path('discussions/<int:pk>/', discussion_details, name='discussion_details'),
    path('discussions/comment/<int:pk>/delete', delete_comment, name='delete_comment'),
    path('discussions/<int:pk>/likes', toggle_like, name='toggle_like'),
    path('discussions/<int:pk>/dislikes', toggle_dislike, name='toggle_dislike'),
]
