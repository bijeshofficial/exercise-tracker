from django.contrib import admin
from .models import Workout, Set, Exercise

# Register your models here.

admin.site.register(Workout)
admin.site.register(Set)
admin.site.register(Exercise)
