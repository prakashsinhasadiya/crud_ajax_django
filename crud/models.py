from django.db import models

class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200,default="")
    number= models.CharField(max_length=10,default="")
    

    def __str__(self):
        return self.name

