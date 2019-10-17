from django.db import models
from django.contrib.auth.models import User

    
class Profile(models.Model):
    picture = models.ImageField(upload_to='picture/', null=True)
    bio = models.CharField(max_length=120)
    
    def save_profile(self):
        self.save()
    
    def update_profile(self):
        self.update()
    
    def delete_profile(self):
        self.delete()
        
       
    
class Comments(models.Model):
    comment_cont = models.CharField(max_length=120)
    
    def save_comment(self):
        self.save
    
    def update_comment(self):
        self.update()
 
    
    
class Image(models.Model):
    image = models.ImageField(upload_to='image/', null=True)
    name = models.CharField(max_length= 60)
    caption = models.CharField(max_length=60, null=True)
    likes = models.IntegerField()
    profile = models.ForeignKey(Profile, null=True)
    comments = models.ForeignKey(Comments, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.image)
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_caption(self):
        self.update()
    
    @classmethod
    def search(cls,id):
        pass 
        
            

