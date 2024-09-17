from django.db import models

class Student(models.Model):
    usn = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Result(models.Model):
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=100)
    cie_marks = models.IntegerField()
    see_marks = models.IntegerField()
    students = models.ManyToManyField(Student, related_name='results')

    def __str__(self):
        return self.subject_name
