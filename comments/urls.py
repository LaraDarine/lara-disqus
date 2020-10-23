from django.urls import path
from .views import comments, comment_details, toggle_like, toggle_dislike


urlpatterns = [
    path('comments/', comments, name='comments'),
    path('comments/<int:pk>/', comment_details, name='comment_details'),
    path('comments/<int:pk>/likes', toggle_like, name='toggle_like'),
    path('comments/<int:pk>/dislikes', toggle_dislike, name='toggle_dislike'),
]
