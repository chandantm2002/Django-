from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    registered_or_not = models.BooleanField(default=False)

    def __str__(self):
        return self.name
