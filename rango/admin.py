from django.contrib import admin
from rango.models import Team, UserProfile, Workout, WorkoutType

# Register your models here.

admin.site.register(Team)
admin.site.register(UserProfile)
admin.site.register(Workout)
admin.site.register(WorkoutType)

