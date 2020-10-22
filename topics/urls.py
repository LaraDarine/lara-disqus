from django.urls import path
from .views import topics


urlpatterns = [
    path('topics/', topics, name='topics'),
]
