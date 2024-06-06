import random

moods = ["Happy", "Sad", "Energetic", "Calm"]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days_of_week:
    mood_today = random.choice(moods)
    print("On", day + ",", "you were feeling", mood_today + ".")


