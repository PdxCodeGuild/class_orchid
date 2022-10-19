from django.db import models
from users.models import CustomUser
from exercise.models import Exercise
# class Planner(models.Model):
#     title = models.CharField(max_length = 200)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE, related_name='user_planner')

class Workout(models.Model):
    day = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.day},{self.user},{self.note}"

class WorkingSet(models.Model):
    # workout_day = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    num_sets = models.IntegerField()
    weight_used = models.IntegerField(null=True, blank=True)
    day = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)