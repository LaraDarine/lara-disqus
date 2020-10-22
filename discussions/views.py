from django.shortcuts import render
from .models import Discussion
from .forms import DiscussionForm


def discussions(request):
    discussions = Discussion.objects.all().order_by('topic')

    context = {
        'discussions': discussions
    }

    return render(request, 'discussions/discussions.html', context)
