from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    date=models.DateField()



def ___str___(self):
    return self.title