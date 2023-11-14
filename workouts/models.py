# workouts/models.py
from django.db import models


class Workout(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def get_day_of_week(self):
        return self.date.strftime('%A')

    def __str__(self):
        day = self.get_day_of_week()
        return f"{day} -> {self.name} on {self.date}"


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.repetitions} * {self.weight} kg"
