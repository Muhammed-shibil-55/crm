from django.db import models


# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField()
    contact=models.CharField(max_length=10,null=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    dob=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name