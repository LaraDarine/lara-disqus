from django.urls import path
from .views import comments, comment_details, toggle_comment_like, toggle_comment_dislike


urlpatterns = [
    path('comments/', comments, name='comments'),
    path('comments/<int:pk>/', comment_details, name='comment_details'),
    path('comments/<int:pk>/likes', toggle_comment_like, name='toggle_comment_like'),
    path('comments/<int:pk>/dislikes', toggle_comment_dislike, name='toggle_comment_dislike'),
]
