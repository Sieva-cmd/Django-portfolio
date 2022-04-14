from django.db import models
from django.forms import CharField
from phone_field import PhoneField

# Create your models here.
class Projects(models.Model):
    title =models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    url =models.URLField(max_length=400)
    image =models.ImageField(upload_to='images/')
    technologies_used =models.CharField(max_length=200,blank=True)


    def __str__(self):
        return f'{self.title} '

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()  


class Profile(models.Model):
    bio = models.TextField(max_length=400, blank=True)
    name = models.CharField(blank=True, max_length=120)
    profile_pic = models.ImageField(upload_to='images/',default='v1639327874/images/default_drurzc.jpg')
    phone_number = PhoneField(max_length=15, blank=True)
    email =models.EmailField(max_length=200)

    
    def __str__(self):
        return f'{self.user.username} Profile'              

    def save_profile(self):
        self.save()    