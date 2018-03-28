import os


def populate():
    u1 = add_user(username='arnold', password='hasapassword')
    add_user_profile(u1, 0, 4000, "Los Angeles")
    u2 = add_user(username='harold', password='hasapassword')
    add_user_profile(u2, 0, 900, "Moscow")
    u3 = add_user(username='john', password='hasapassword')
    add_user_profile(u2, 10.1, 765, "Cape Town")

    w1 = add_workout_type('deadlift', False)
    add_workout_type('squat', False)
    w2 = add_workout_type('pushup', False)
    add_workout_type('curl', False)

    add_workout_type('rowing', True)
    add_workout_type('cycling', True)
    add_workout_type('running', True)
    w3 = add_workout_type('walking', True)

    add_workout(u1, w1, 10, 4, 100, 0, 0)
    add_workout(u2, w2, 20, 3, 15, 0, 0)
    add_workout(u3, w3, 0, 0, 0, 10, 0.01)
    add_workout(u3, w1, 15, 3, 17, 0, 0)

    add_team([u1, u2], "Elderly", "Elderly")
    add_team([u1, u3], "Buff", "Buff")
    add_team([u2], "LonelyPeople", "Lonely People")


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
    u_p = UserProfile.objects.get_or_create(user=user, distancepoints=dp, weightpoints=wp, location=location)
    return u_p


def add_user(username, password):
    u = User.objects.get_or_create(username=username, password=password)
    return u


if __name__ == '__main__':
    print("Starting database population!")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wwworkout.settings')
    from rango.models import *

    populate()
