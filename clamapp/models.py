from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

    
class Profile(models.Model):
    picture = models.ImageField(upload_to='picture/', null=True)
    bio = models.CharField(max_length=120)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.bio)
    
    def save_profile(self):
        self.save()
    
    def update_profile(self):
        self.update()
    
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def search(cls,search_term):
        print(f'hello search term model {search_term}')

        username = cls.objects.filter(user__username__icontains=search_term)
        return username   
        
 
class Image(models.Model):
    image = models.ImageField(upload_to='image/', null=True)
    name = models.CharField(max_length= 60, null=True)
    caption = models.CharField(max_length=60, null=True)
    likes = models.IntegerField()
    profile = models.ForeignKey(Profile, null=True)
    # comments = models.ForeignKey(Comments, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = HTMLField()
    
    def __str__(self):
        return str(self.image)
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_caption(self):
        self.update()
    
    @classmethod
    def get_all_image(cls):
        img = cls.objects.all().prefetch_related('comments_set')
        return img
    
  
class Comments(models.Model):
    comment_cont = models.CharField(max_length=120)
    commented_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    commented_image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    
    def save_comment(self):
        self.save
    
    def update_comment(self):
        self.update()
        
    def delete_comment(self):
        self.delete()       
        
class Follow(models.Model):
    user = models.ForeignKey(User, null=True)
    followers = models.ForeignKey(Profile, related_name='following', null=True)
    following = models.ForeignKey(Profile, related_name='followers', null=True) 
    
    def save_follow(self):
        self.save()
    
    @classmethod
    def get_followers(cls):
        follower = cls.objects.all()
        return follower
    
    @classmethod
    def get_following(cls):
        following = cls.objects.all()
        return following     
            

