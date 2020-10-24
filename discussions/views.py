from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Discussion
from .forms import DiscussionForm
from comments.forms import CommentForm

def home(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect(discussions)
    else:
        return render(request, 'discussions/welcome.html')

def discussions(request):
    discussions = Discussion.objects.all().order_by('topic')

    context = {
        'discussions': discussions,
        'current_user': request.user
    }

    return render(request, 'discussions/discussions.html', context)

def discussion_details(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    current_user = request.user

    if current_user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form.add_comment(current_user, discussion)
                context = {
                    'discussion': discussion,
                    'current_user': request.user,
                    'comment_form': comment_form
                }
                return render(request, 'discussions/discussion-details.html', context)
            else:
                pass
    comment_form = CommentForm()
    context = {
        'discussion': discussion,
        'current_user': request.user,
        'comment_form': comment_form
    }

    return render(request, 'discussions/discussion-details.html', context)

#TODO: Make this view func globally
def toggle_like(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        discussion = get_object_or_404(Discussion, pk=pk)
        print(discussion.likes)
        
        if discussion.likes.filter(id=current_user.id).exists():
            discussion.likes.remove(current_user.id)
        else:
            discussion.likes.add(current_user.id)
            if discussion.dislikes.filter(id=current_user.id).exists():
                discussion.dislikes.remove(current_user.id)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def toggle_dislike(request, pk):
    current_user = request.user
    if current_user.is_authenticated:
        discussion = get_object_or_404(Discussion, pk=pk)
        print(discussion.dislikes)
        
        if discussion.dislikes.filter(id=current_user.id).exists():
            discussion.dislikes.remove(current_user.id)
        else:
            discussion.dislikes.add(current_user.id)
            if discussion.likes.filter(id=current_user.id).exists():
                discussion.likes.remove(current_user.id)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
