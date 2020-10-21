from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='topics/', default='topics/topic.png')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title