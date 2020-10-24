from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Reply
from .forms import ReplyForm


def replies(request):
    replies = Reply.objects.all().order_by('comment')

    context = {
        'replies': replies,
        'current_user': request.user
    }

    return render(request, 'replies/replies.html', context)

def reply_details(request, pk):
    reply = get_object_or_404(Reply, pk=pk)

    context = {
        'reply': reply,
        'current_user': request.user
    }

    return render(request, 'replies/reply-details.html', context)

#TODO: Make this view func globally
def toggle_reply_like(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        reply = get_object_or_404(Reply, pk=pk)
        
        if reply.likes.filter(id=current_user.id).exists():
            reply.likes.remove(current_user.id)
        else:
            reply.likes.add(current_user.id)
            if reply.dislikes.filter(id=current_user.id).exists():
                reply.dislikes.remove(current_user.id)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def toggle_reply_dislike(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        reply = get_object_or_404(Reply, pk=pk)
        print(reply.dislikes)
        
        if reply.dislikes.filter(id=current_user.id).exists():
            reply.dislikes.remove(current_user.id)
        else:
            reply.dislikes.add(current_user.id)
            if reply.likes.filter(id=current_user.id).exists():
                reply.likes.remove(current_user.id)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
