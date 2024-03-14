
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user_image= models.FileField(upload_to="static/user_image")
    contact=models.IntegerField(null=True,blank=True)
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username

class Post(models.Model):
    image=models.FileField(upload_to="static/img")
    caption=models.CharField(max_length=150,null=True,blank=True)
    date=models.DateTimeField(auto_now=False,auto_now_add=False)
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
