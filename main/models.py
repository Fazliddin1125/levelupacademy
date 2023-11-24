from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    month = models.FloatField()
    price = models.FloatField()
    student = models.IntegerField()
    title = models.CharField(max_length=150, default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aspernatur, fuga?')

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    checked = models.BooleanField(default=False, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

