from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # additional attributes
    # userid = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # owner = models.BooleanField
    distancepoints = models.DecimalField(max_digits=8, decimal_places=2)
    weightpoints = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.user.username


class Team(models.Model):
    # Links Teams and Users model instance.
    user = models.ManyToManyField(User)

    # additional attributes
    teamid = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='team_images', blank=True)

    def save(self, *args, **kwargs):
        self.teamid = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


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


    def __str__(self):
        return self.workoutid