from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Discussion
from .forms import DiscussionForm


def discussions(request):
    discussions = Discussion.objects.all().order_by('topic')

    context = {
        'discussions': discussions
    }

    return render(request, 'discussions/discussions.html', context)

def toggle_like(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        discussion = get_object_or_404(Discussion, pk=pk)
        print(discussion.likes)
        
        if discussion.likes.filter(id=current_user.id).exists():
            discussion.likes.remove(current_user.id)
        else:
            discussion.likes.add(current_user.id)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
