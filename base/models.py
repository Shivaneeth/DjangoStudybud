from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # save every time
    created = models.DateTimeField(auto_now_add=True)  # save only when created
    # participants

    class Meta:
        # ordering based on field, '-' repesents reverse order
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # One to many relation
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # save every time
    created = models.DateTimeField(auto_now_add=True)  # save only when created

    def __str__(self) -> str:
        return self.body[0:50]
