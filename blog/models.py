from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import login,logout,authenticate
from ckeditor.fields import RichTextField

import uuid

 
# Create your models here.

     

class CustomUserManager(BaseUserManager):

     def create_user(self,username, email,password, *args,**extra_fields):
          
          if not email:
               raise ValueError("Email must be Set")
          email = self.normalize_email(email)
          user = self.models(username=username,email=email,*args,**extra_fields)
          user.set_password(password)
          user.save()
          return user

     def create_superuser(self,email,password,*args,**extra_fields):
          extra_fields.setdefault('is_staff',True)
          extra_fields.setdefault('is_superuser',True)
          return self.create_user(self,email,password,*args,**extra_fields)

class CustomBlogUser(AbstractUser):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     fullname =  models.CharField(max_length=50)
     bio =  models.TextField(max_length=150,blank=True,null=True)
     levelofAuthor = {
          (1, "Level 1 Author"),
          (2, "Level 2 Author"),
          (3, "Level 3 Author"),
     }

     profile_picture = CloudinaryField('Image',overwrite=True,format="png",blank=True,null=True)
     authorLevel =  models.IntegerField(choices=levelofAuthor,default=1)
     total_followers = models.PositiveIntegerField(default=0,blank=True,null=True) 
     total_following = models.PositiveIntegerField(default=0,blank=True,null=True)
     totalpost = models.PositiveIntegerField(default=0,blank=True,null=True)
     totalcomment = models.PositiveIntegerField(default=0,blank=True,null=True)
     totalreply = models.PositiveIntegerField(default=0,blank=True,null=True)
     socialLink1 =  models.URLField(blank=True,null=True)
     socialLink2 =  models.URLField(blank=True,null=True)
     socialLink3 =  models.URLField(blank=True,null=True)
     updated_at = models.DateTimeField(auto_now=True)
     is_staff = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)
 
     obj = CustomUserManager()

     class Meta:
          ordering = ('-date_joined',)
     
     def __str__(self):
          return self.username
     
     def save(self,*args, **kwargs):
          if not self.username:
               to_assaign = "".join(self.fullname.split(" ")).lower()

               if CustomBlogUser.objects.filter(username=to_assaign).exists():

                    to_assaign = to_assaign+str(CustomBlogUser.objects.all().count())
               
               self.username = to_assaign

          total_Post = Post.objects.filter(user__username=self.username).count() 
          total_Comment =  Comment.objects.filter(user__username=self.username).count()
          total_reply =  Reply.objects.filter(user__username=self.username).count()
          totalFollowing =  user_follow.objects.filter(follower__username=self.username).count()
          totalFollowers =  user_follow.objects.filter(following__username=self.username).count()
          self.totalpost = total_Post
          self.totalcomment =  total_Comment
          self.totalreply =  total_reply
          self.total_following =  totalFollowing
          self.total_followers =  totalFollowers


          if not self.fullname and self.first_name and self.last_name:   
                 self.fullname =  self.get_full_name();

          super().save(*args,**kwargs)

 


         

  

class Post(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     user =  models.ForeignKey(to=CustomBlogUser,  on_delete=models.DO_NOTHING)
     title = models.CharField(max_length=200)
     summary = models.CharField(max_length=500,blank=True,null=True)
     description =  RichTextField()
     slug = models.SlugField(max_length=255, blank=True,null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     featureImage = CloudinaryField('FeatureImage',overwrite=True,format="png",blank=True,null=True)

     class Meta:
          ordering = ('-created_at',)
     
     def __str__(self):
          return self.title
     
     def save(self,*args, **kwargs):
          to_assaign = slugify(self.title)

          if Post.objects.filter(slug = to_assaign).exists():

               to_assaign = to_assaign+str(Post.objects.all().count())
          
          self.slug = to_assaign

          if not self.summary:
               words = self.description.split()[:30]
               self.summary = ' '.join(words)
          

          super().save(*args,**kwargs)

class Comment(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     post =  models.ForeignKey(to=Post,  on_delete=models.CASCADE)
     user =  models.ForeignKey(to=CustomBlogUser,  on_delete=models.CASCADE)
     comment = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
          ordering = ('-created_at',)
     
     def __str__(self):
          return self.comment
     
class Reply(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     comment =  models.ForeignKey(to=Comment,  on_delete=models.CASCADE)
     user =  models.ForeignKey(to=CustomBlogUser,  on_delete=models.CASCADE)
     reply = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
          ordering = ('-created_at',)
     
     def __str__(self):
          return self.reply
     
class user_follow(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     following =  models.ForeignKey(to=CustomBlogUser,  on_delete=models.CASCADE,related_name='main_user')
     follower =  models.ForeignKey(to=CustomBlogUser,  on_delete=models.CASCADE,related_name="follower_user")
     subscribed_date = models.DateTimeField(auto_now_add=True)

     class Meta:
          ordering = ('-subscribed_date',)
          unique_together = (('follower','following'),)
     
  
     
 

         





