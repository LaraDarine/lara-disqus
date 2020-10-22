from django.shortcuts import render
from .models import Topic


def topics(request):
    topics = Topic.objects.all()

    context = {
        'topics': topics
    }

    return render(request, 'topics/topics.html', context)
