from django.shortcuts import render
from .models import Topic


def topics(request):
    topics = Topic.objects.all().order_by('topic')

    context = {
        'topics': topics
    }

    return render(request, 'topics/topics.html', context)
