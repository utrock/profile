from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    desc =models.CharField(max_length=100)
    image=models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    #blank isliye taki vo field optional bn jae



    def ___str___(self):
        return self.title


class Imga(models.Model):
     image=models.ImageField(upload_to='portfolio/imagess/')
    