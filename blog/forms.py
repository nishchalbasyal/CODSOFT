from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = CustomBlogUser
#         Fields = [
#             'email',
#             'fullname',
#             'password',
#             'ProfilePicture'

#         ]

class AddPost(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=Post
        fields = ["title","summary","description","featureImage"]

 
        
    
 