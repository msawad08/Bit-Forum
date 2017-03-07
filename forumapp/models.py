from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType


# Create your models here.

class Post(models.Model):
    class Meta:
        abstract = True

    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=False, auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    upVote = models.PositiveIntegerField(default=0)
    downVote = models.PositiveIntegerField(default=0)
    text = models.TextField()

    def get_content_type(self):
        return ContentType.objects.get_for_model(self).id


class Question(Post):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Answer(Post):
    answerOf = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=False, auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    text = models.TextField
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')





