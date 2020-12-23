from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length = 12, default= 'NONE')
    address = models.CharField(max_length = 20,default = 'NONE')
    city = models.CharField(max_length = 20,default = 'NONE')
    state = models.CharField(max_length = 20,default = 'NONE')
    image = models.ImageField(default='default.jpg', upload_to='images')

    def __str__(self):
        return f'{self.user.username} Profile'

 #   def save(self,*args,**kwargs):
  #      super().save(*args,**kwargs)
#
 #       img = Image.open(self.image.path)
#
 #       if img.height >300 or img. width >300:
  #          output_size = (300,300)
   #         img.thumbnail(output_size)
    #        img.save(self.image.path)