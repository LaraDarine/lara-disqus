from django.urls import path
from .views import discussions, discussion_details, toggle_like, toggle_dislike, home, delete_comment, edit_comment, toggle_order


urlpatterns = [
    path('discussions/welcome', home, name='home'),
    path('discussions/', discussions, name='discussions'),
    path('discussions/<int:pk>/', discussion_details, name='discussion_details'),
    path('discussions/comment/<int:pk>/delete', delete_comment, name='delete_comment'),
    path('discussions/comment/<int:pk>/edit', edit_comment, name='edit_comment'),
    path('discussions/<int:pk>/likes', toggle_like, name='toggle_like'),
    path('discussions/<int:pk>/dislikes', toggle_dislike, name='toggle_dislike'),
    path('discussions/<int:pk>/dislikes', toggle_dislike, name='toggle_dislike'),
    path('discussions/toggle_order', toggle_order, name='toggle_order'),
]
