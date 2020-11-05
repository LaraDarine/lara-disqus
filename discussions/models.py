from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()


class Discussion(models.Model):
    author = models.ForeignKey(
        User,
        related_name='author',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(
        upload_to='discussions/',
        default='discussions/discussion.png')
    demo_image = models.ImageField(
        upload_to='discussions/',
        default='discussions/discussion.png')
    likes = models.ManyToManyField(
        User,
        related_name='likes',
        blank=True
        )
    dislikes = models.ManyToManyField(
        User,
        related_name='dislikes',
        blank=True
        )

    class _Meta:
        ordering = ('id',)

    def __str__(self):
        return f'{self.author.username}-{self.title}-{self.created_at}'

    def likes_count(self):
        return self.likes.count()

    def dislikes_count(self):
        return self.dislikes.count()
    
    def comments_count(self):
        return self.get_comments().count()

    def get_comments(self):
        from comments.models import Comment
        comments = Comment.objects.filter(discussion=self, parent=None)
        
        return comments
    
    def order_comments(self, user):
        if user.profile.best_comments_order:
            best_comments = self.get_comments().annotate(
                num_likes=Count('likes')).order_by('-num_likes')
            return best_comments
        else:
            latest_comments = self.get_comments().order_by('-created_at')
            return latest_comments
