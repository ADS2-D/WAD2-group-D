from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    userid = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    owner = models.BooleanField
    distancepoints = models.DecimalField(max_digits=3, decimal_places=2)
    weightpoints = models.DecimalField(max_digits=3, decimal_places=2)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username


class Teams(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    teams = models.ManyToManyField(User)

    # The additional attributes we wish to include.
    teamid = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.teamid


class Workout(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    workout = models.ForeignKey(User)

    # The additional attributes we wish to include.
    workoutid = models.CharField(max_length=30)
    distance = models.IntegerField
    reps = models.IntegerField
    sets = models.IntegerField
    weights = models.IntegerField
    cadence = models.DecimalField(max_digits=3, decimal_places=2)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.workoutid