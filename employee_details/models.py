from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.title}'

class Employee(models.Model):
    fullname = models.CharField(max_length=150)
    emp_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fullname} ' + f'{self.mobile}'

