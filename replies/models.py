from django.db import models
from comments.models import Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment,
        related_name='comment',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        related_name='reply_author',
        on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='replies/',
        blank=True
        )
    likes = models.ManyToManyField(
        User,
        related_name='reply_likes',
        blank=True
        )
    dislikes = models.ManyToManyField(
        User,
        related_name='reply_dislikes',
        blank=True
        )

    def __str__(self):
        return f'{self.author.username}-{self.created_at}'

    def likes_count(self):
        return self.likes.count()

    def dislikes_count(self):
        return self.dislikes.count()
