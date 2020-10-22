from django.shortcuts import render
from .models import Discussion
from .forms import DiscussionForm


def discussions(request):
    discussions = Discussion.objects.all()

    context = {
        'discussions': discussions
    }

    return render(request, 'discussions/discussions.html', context)
