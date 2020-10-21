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
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='discussions/',
        default='discussions/discussion.png')


    def __str__(self):
        return f'{self.author.username} - {self.topic.title} - {self.created_at}'
    

    def get_comments(self):
        from comments.models import Comment
        comments = Comment.objects.filter(post=self)
        return comments
