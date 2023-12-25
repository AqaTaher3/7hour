from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)


class Room(models.Model):
    host = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return str(self.id)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='room_mess')
    body = models.TextField(null=True, blank=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
