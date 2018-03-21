from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import uuid


# Create your models here.

class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # additional attributes
    # userid = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # owner = models.BooleanField
    distancepoints = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    weightpoints = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username


class Team(models.Model):
    # Links Teams and Users model instance.
    user = models.ManyToManyField(User)

    # additional attributes
    team_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='team_images', blank=True)

    def save(self, *args, **kwargs):
        self.teamid = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class WorkoutType(models.Model):
    name = models.CharField
    cardio = models.NullBooleanField
    weights = models.NullBooleanField


class Workout(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.ForeignKey(User)
    workoutType = models.ForeignKey(WorkoutType)

    # The additional attributes we wish to include.
    workoutid = models.CharField(max_length=12, unique=True, default=uuid.uuid4())
    picture = models.ImageField(upload_to='profile_images', blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    reps = models.IntegerField
    sets = models.IntegerField
    weights = models.IntegerField
    weight_points = models.IntegerField

    distance = models.IntegerField
    cadence = models.DecimalField(max_digits=3, decimal_places=2)
    cardio_points = models.IntegerField

    def __str__(self):
        return self.workoutid
