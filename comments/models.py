from django.db import models
from discussions.models import Discussion
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    discussion = models.ForeignKey(
        Discussion,
        related_name='discussion',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        related_name='comment_author',
        on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',
        related_name='replies',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    image = models.ImageField(
        upload_to='comments/',
        blank=True
        )
    likes = models.ManyToManyField(
        User,
        related_name='comment_likes',
        blank=True
        )
    dislikes = models.ManyToManyField(
        User,
        related_name='comment_dislikes',
        blank=True
        )

    def __str__(self):
        return f'{self.author.username}-{self.created_at}'
    
    @property
    def is_comment(self):
        return self.parent is None

    def likes_count(self):
        return self.likes.count()

    def dislikes_count(self):
        return self.dislikes.count()