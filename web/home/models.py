from django.db import models

# Create your models here.
class apply(models.Model):
    name=models.CharField(max_length=122)
    department=models.CharField(max_length=122)
    location=models.CharField(max_length=122)
    details=models.CharField(max_length=1000)
    img1 = models.ImageField(upload_to = "image1/")
    img2 = models.ImageField(upload_to = "image2/",null=True,blank=True)
    date=models.DateField()

   

    def __str__(self):
        return self.name