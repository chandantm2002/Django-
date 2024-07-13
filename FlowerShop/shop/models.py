from django.db import models

class Flower(models.Model):
    flower_name = models.CharField(max_length=100)
    flower_type = models.CharField(max_length=100)
    age = models.IntegerField()
    features = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.flower_name

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    cphone = models.CharField(max_length=15)
    cemail = models.EmailField()
    cf = models.ManyToManyField(Flower, through='Purchase')

    def __str__(self):
        return self.customer_name

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} bought {self.flower}'
