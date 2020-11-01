from django.db import models
from topics.models import Topic
from django.contrib.auth import get_user_model

User = get_user_model()


class Discussion(models.Model):
    topic = models.ForeignKey(
        Topic,
        related_name='topic',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        related_name='author',
        on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
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
        return f'{self.author.username}-{self.topic.title}-{self.created_at}'

    def likes_count(self):
        return self.likes.count()

    def dislikes_count(self):
        return self.dislikes.count()

    def get_comments(self):
        from comments.models import Comment
        comments = Comment.objects.filter(discussion=self, parent=None)
        
        return comments
