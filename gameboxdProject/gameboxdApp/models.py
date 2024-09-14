from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# database table for the games a user can review
class Game(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


# database table for a user's reviews
class Review(models.Model):
    title = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField()
    like = models.BooleanField(default=False)
    review = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

