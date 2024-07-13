from django.db import models

class Bank(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    aadhar = models.BigIntegerField()
    pincode = models.IntegerField()

    def __str__(self):
        return f"{self.fname} {self.lname}"
