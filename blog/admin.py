from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *;

# Register your models here.

class BlogPostInline(admin.TabularInline):
    model = Post
class CommentInline(admin.TabularInline):
    model = Comment
class ReplyInline(admin.TabularInline):
   model = Reply

class UserModelAdmin(UserAdmin):
    list_display = ('username','email','date_joined','is_staff','is_superuser')
    fieldsets = (
        (None, {
            "fields": (
                'username','password','profile_picture','email','fullname','bio',('totalpost','totalcomment','totalreply'),('authorLevel','total_followers','total_following'),'socialLink1','socialLink2','socialLink3'
            ),
        }),
        ('Permissions',{"fields":(
            'is_staff',('is_active','is_superuser'),
        )}),
        (
            'Advanced options',{
                'classes':('collapse',),
                'fields':('groups','user_permissions'),
            }
        )
    )
    
    # inlines = [
    #     BlogPostInline,CommentInline,ReplyInline
    # ]
    search_fields = ('username','email','first_name','last_name','fullname')
    ordering = ('date_joined',)

    def get_post(self,obj):
        return obj.Post
    
    search_fields = ('fullname','email','username')
    list_per_page = 10

    
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','user','created_at')
    search_fields = ('title','user__email','description','user__fullname','user__email')
    list_per_page = 10
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('post','user','comment','created_at')
    search_fields = ('title','user__email','description','user__fullname','user__email','slug')
    list_per_page = 10
class ReplyModelAdmin(admin.ModelAdmin):
    list_display = ('comment','user','created_at')
    search_fields = ('post__title','user__email','user__fullname','user__email','comment__comment')
    list_per_page = 10
class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('following','follower','subscribed_date')
    list_per_page = 10



admin.site.register(CustomBlogUser,UserModelAdmin)
admin.site.register(Post,PostModelAdmin)
admin.site.register(Comment,CommentModelAdmin)
admin.site.register(Reply,ReplyModelAdmin)
admin.site.register(user_follow,UserFollowAdmin)
