from django.test import TestCase
from .models import Image, Profile, Comments, Follow
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    '''
    a class to test the Profile functionality and it's class
    '''
    def setUp(self):
        self.user= User.objects.create(id='1',username='stacy')
        self.picture = Profile(picture='picture/', bio='myself', user=self.user)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.picture, Profile))  
        
    def test_save_profile(self):
        self.picture.save_profile()
        pic = Profile.objects.all()
        self.assertTrue(len(pic)>0) 
        
    def test_update_profile(self):
        self.picture.save_profile()
        profile = Profile.objects.filter(bio='myself').first()
        update = Profile.objects.filter(bio = profile.bio).update(bio='me')
        updated = Profile.objects.filter(bio = 'me').first()
        self.assertNotEqual(profile.bio, updated.bio)   
        
    def test_delete_profile(self):
        self.picture.save()
        profile = Profile.objects.filter(bio='myself').first()
        delete = Profile.objects.filter(bio=profile.bio).delete()
        profiles = Profile.objects.all()
        self.assertFalse(len(profiles) == 1)      

class CommentsTestClass(TestCase):
    '''
    a class to test the functionalities and instances of Comment class
    '''
    def setUp(self):
        self.user = User.objects.create(id='1', username='clarisse')
        self.image = Image.objects.create(image='image/', name='e', caption='u',likes='1',post='hello',user=self.user)
        self.profile = Profile.objects.create(picture='picture/', bio='myself', user=self.user)
        self.comment= Comments.objects.create(comment_cont='nice', commented_by = self.profile,commented_image=self.image)
        
                
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.image, Image))
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertTrue(isinstance(self.comment, Comments))
    
    def test_save_comment(self):
        self.comment.save_comment()
        com = Comments.objects.all()
        self.assertTrue(len(com)>0)  
        
    def test_delete_comment(self):
        self.comment.save()
        comment = Comments.objects.filter(comment_cont='nice').first()
        delete = Comments.objects.filter(comment_cont=comment.comment_cont).delete()
        comments = Comments.objects.all()
        self.assertFalse(len(comments) == 1)     
                
class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id='1', username='stacy')
        self.profile = Profile.objects.create(picture='picture/', bio='myself', user=self.user)
        self.image = Image.objects.create(image='image/', name='me', caption='myFoto',likes='1', profile=self.profile,post='hello', user=self.user)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertTrue(isinstance(self.image, Image))
    
    def test_save_image(self):
        self.image.save_image()
        img = Image.objects.all()
        self.assertTrue(len(img)>0) 
        
    def test_update_image(self):
        self.image.save_image()
        image = Image.objects.filter(caption='myFoto').first()
        update = Image.objects.filter(caption = image.caption).update(caption='foto')
        updated = Image.objects.filter(caption = 'foto').first()
        self.assertNotEqual(image.caption, updated.caption)   
        
    def test_delete_profile(self):
        self.image.save_image()
        image = Image.objects.filter(caption='myFoto').first()
        delete = Image.objects.filter(caption=image.caption).delete()
        images = Image.objects.all()
        self.assertFalse(len(images) == 1)    
        
        
        
