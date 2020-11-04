from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import Discussion
from .forms import DiscussionForm
from comments.models import Comment
from comments.forms import CommentForm

def home(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect(discussions)
    else:
        return render(request, 'discussions/welcome.html')

def discussions(request):
    discussions = Discussion.objects.all().order_by('id')

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
            comment_form = CommentForm(request.POST, request.FILES)

            parent_comment = None
            if comment_form.is_valid():
                try:
                    parent_comment_id = int(request.POST.get('parent_id'))
                except:
                    parent_comment_id = None

                if parent_comment_id:
                    parent_comment = Comment.objects.get(id=parent_comment_id)

                    if parent_comment:
                        reply_form = comment_form.save(commit=False)
                        reply_form.parent = parent_comment
                        reply_form = CommentForm()
                
                comment_form.add_comment(current_user, discussion)
                context = {
                    'discussion': discussion,
                    'current_user': request.user,
                    'comment_form': comment_form
                }
                return HttpResponseRedirect(request.path_info)

    comment_form = CommentForm()
    ordered_comments = discussion.get_comments().order_by('created_at').all()
    context = {
        'discussion': discussion,
        'current_user': request.user,
        'ordered_comments': ordered_comments,
        'comment_form': comment_form
    }

    return render(request, 'discussions/discussion-details.html', context)

def edit_comment(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST, request.FILES, instance=comment)

            if comment_form.is_valid():
                comment_form.save()
                return redirect('discussion_details', pk=comment.discussion.id)
        else:
            comment_form = CommentForm(instance=comment)

        
        context = {
            'comment': comment,
            'comment_form': comment_form
        }

        return render(request, 'discussions/edit-comment.html', context)
    else:
        return redirect('home')

def delete_comment(request, pk):
    if request.user.is_authenticated:

        comment = get_object_or_404(Comment, pk=pk)
        discussion_id = comment.discussion.id
        comment.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')

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
