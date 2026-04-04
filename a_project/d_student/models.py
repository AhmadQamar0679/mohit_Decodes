from django.db import models

# Create your models here.

class Department(models.Model):
    dep_name=models.CharField(max_length=100)

    def __str__(self):
        return str(self.dep_name)



class Student_detail(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    
    


    def __str__(self):
        return self.name
