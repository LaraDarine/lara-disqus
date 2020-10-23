from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Comment
from .forms import CommentForm


def comments(request):
    comments = Comment.objects.all().order_by('discussion')

    context = {
        'comments': comments,
        'current_user': request.user
    }

    return render(request, 'comments/comments.html', context)

def comment_details(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    context = {
        'comment': comment,
        'current_user': request.user
    }

    return render(request, 'comments/comment-details.html', context)

#TODO: Make this view func globally
def toggle_like(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)
        print(comment.comment_likes)
        
        if comment.comment_likes.filter(id=current_user.id).exists():
            comment.comment_likes.remove(current_user.id)
        else:
            comment.comment_likes.add(current_user.id)
            if comment.comment_dislikes.filter(id=current_user.id).exists():
                comment.comment_dislikes.remove(current_user.id)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def toggle_dislike(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)
        print(comment.comment_dislikes)
        
        if comment.comment_dislikes.filter(id=current_user.id).exists():
            comment.comment_dislikes.remove(current_user.id)
        else:
            comment.comment_dislikes.add(current_user.id)
            if comment.comment_likes.filter(id=current_user.id).exists():
                comment.comment_likes.remove(current_user.id)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
