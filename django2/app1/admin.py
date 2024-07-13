from django.contrib import admin

# Register your models here.
from .models import students
admin.site.register(students)
def __str__(self):
        return self.name1