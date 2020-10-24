from django.urls import path
from .views import replies, reply_details, toggle_reply_like, toggle_reply_dislike


urlpatterns = [
    path('replies/<int:pk>/', reply_details, name='reply_details'),
    path('replies/<int:pk>/likes', toggle_reply_like, name='toggle_reply_like'),
    path('replies/<int:pk>/dislikes', toggle_reply_dislike, name='toggle_reply_dislike'),
]
