from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20,default='')
    message=models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.name
    
class Projects(models.Model):
    name=models.CharField(max_length=80)
    photo=models.ImageField(upload_to='image',default='/static/images/done.jpg')
    url=models.CharField(max_length=400)
    github=models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.name