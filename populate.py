import os


def add_team(users, team_id, name):
    t = Team.objects.get_or_create(team_id=team_id, name=name)
    for u in users:
        t.users.add(u)

    return t


def add_workout(user, workoutType, reps, sets, weights, distance, cadence):
    weightpoints = reps * sets * weights
    distancepoints = distance * (1 + cadence)
    w = Workout.objects.get_or_create(user=user, workoutType=workoutType, reps=reps, sets=sets, weights=weights,
                                      weight_points=weightpoints, distance=distance, cadence=cadence,
                                      distance_points=distancepoints)
    return w


def add_workout_type(name, cardio):
    wt = WorkoutType.objects.get_or_create(name=name, cardio=cardio, weights=not cardio)
    return wt


def add_user_profile(user, dp, wp, location):
    u_p = UserProfile.objects.get_or_create(user=user, distancepoints=dp, weightpoints=dp, location=location)
    return u_p


def add_user(username, password):
    u = User.objects.get_or_create(username=username, password=password)
    return u


if __name__ == '__main__':
    print("Starting database population!")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wwworkout.settings')
    from rango.models import *
