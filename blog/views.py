from django.shortcuts import render,get_object_or_404,HttpResponseRedirect, HttpResponse,redirect
from .models import *
from cloudinary import uploader
from django.contrib.auth import authenticate 

from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.hashers import make_password,check_password
from django.core import serializers

from django.core.paginator import Paginator


import json

from .forms import AddPost
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.template import loader
import re






# Create your views here.

def Reusable_Context(request):
        context = {};
        if request.user.is_authenticated:
            context['authenticated'] = True
            username  = request.user.username
            user = CustomBlogUser.objects.get(username=username)
            context['user'] =  user
            context['fullname'] = user.fullname
            context['profile_picture'] = user.profile_picture
            context['username'] = request.user.username
        else:
            context['authenticated'] = False
        return context


 
def home(request):
    context = Reusable_Context(request)      
    allPost = Post.objects.all()
    context['allPost'] = allPost
       
    return render(request,"home.html" ,context);


class LoginViewUser(LoginView):
    template_name = "registration/login.html"
 
    def form_valid(self, form):
         if self.request.user.is_authenticated:
             print('user authonicated')
             return redirect("author.url",username=self.request.user.username)
         return super().form_valid(form)
  
       
    

 
    

    



    


    
    # if request.method == "POST":
    #     email = request.POST.get("email");
    #     password = request.POST.get("password");
    #     try:
    #         user = login(request,user)
    #         print(user)
    #         if user:
    #              request.session["user"] = user
    #         else:
    #             return HttpResponse("<h1>Session Not Created</h1>")
    #         return HttpResponseRedirect("/")
    #     except Exception as e:                
    #            user =  None
    #            return HttpResponse(e)
            
        
        
    # return render(request,"login.html")


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        fullname = request.POST.get("fullname")
        password = request.POST.get("password")
        profile_picture = request.FILES.get("file")
        username = "".join(fullname.split(" ")).lower()

  
        if(email == '' or username== '' or fullname == '' or password == ''):
            return HttpResponseRedirect("/register")
        else:
            new_user = CustomBlogUser.objects.create_user(
                username=username,
                email=email,
                fullname=fullname,
                password=password,
                profile_picture=profile_picture
            )
            if new_user:
                return  HttpResponseRedirect("/login")
            else:
                return HttpResponse("Something went wrong")
        


    return render(request,"register.html")


class Add_Post(LoginRequiredMixin,CreateView):
    model=Post
    form_class=AddPost
    template_name="write.html"
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    

class Update_View(LoginRequiredMixin,UpdateView):
    model=Post
    form_class=AddPost
    template_name="update.html"
    success_url = '/'
    redirect_field_name = "/login"


    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            # Redirect to a different URL or display an error message
            return HttpResponseRedirect(f"/{self.object.slug}")
        return super().get(request, *args, **kwargs)





    
def author_view(request,username):
    context = Reusable_Context(request)
    author = CustomBlogUser.objects.get(username=username)
    currentUserFollowingList = None;
    currentUser = "";

    if request.user.username:
        currentUser = CustomBlogUser.objects.get(username=context['username'])
        currentUserFollowingList = user_follow.objects.filter(follower=currentUser)

    posts = Post.objects.filter(user=author)
    followingList = user_follow.objects.filter(follower=author)


    context["author"] = author
    context["posts"] = posts
    isAlreadyFollow = False


    current_user =  request.GET.get('currentUser')
    author_r =  request.GET.get('currentUser')
   
    if currentUser and currentUserFollowingList: 
        if currentUserFollowingList.filter(following=author).exists():
            isAlreadyFollow = True

    context["isAlreadyFollow"] = isAlreadyFollow
    paginator = Paginator(followingList,10)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context["page"] = page

    if(current_user and author_r):
        if isAlreadyFollow:
            try:
                user = user_follow.objects.get(follower=currentUser, following=author)
                user.delete()
                response_data = {'status': 'unfollowed'}
                return JsonResponse(response_data, status=200)
            except user_follow.DoesNotExist:
                response_data = {'status': 'error'}

                return JsonResponse(response_data, status=404)
        else:
            new_follow = user_follow(follower=currentUser, following=author)
            new_follow.save()
            response_data = {'status': 'followed'}
            return JsonResponse(response_data, status=200)




    return render(request, "author.html",context)



   

def search_view(request):
    searchText = request.GET.get("keywords")
    context = {}
    template =  loader.get_template('SearchPage.html')
    if searchText:
        cleaned_search_text = re.sub(r'[^a-zA-Z0-9 ]', '', searchText).lower()

        try:
            results =  Post.objects.filter(
                Q(title__icontains=cleaned_search_text)|Q(summary__icontains=cleaned_search_text)|Q(user__username__icontains=cleaned_search_text)
                
                )
            context["Posts"] = results

         
        except:
            context["Posts"] = None;
    
    return HttpResponse(template.render(context,request))

 
def delete_view(request,slug):
    post = get_object_or_404(Post, slug=slug)

    if post.user == request.user:
        post.delete()


    return redirect('author.url',username=request.user.username)
def single_post(request, slug):
    context = Reusable_Context(request)
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)
    replies = Reply.objects.filter(comment__in=comments)
    context['post'] = post
    context['allComments'] = comments
    context['totalcomments'] = comments.count()
    context['allReplies'] = replies
 
  
    return render(request, "post.html",context)
 

def comment(request,slug):
    if request.method == "POST":
       slug = slug
       comment = request.POST.get("comment")
       username = request.user.username
       try:
            if comment:
                post = Post.objects.get(slug=slug)
                user = CustomBlogUser.objects.get(username=username)
                newComment = Comment(
                    user=user,
                    post=post,
                    comment=comment
                )
                newComment.save()
            return HttpResponseRedirect(f"/{slug}")
       except Exception as e:
           print(Exception)

           
        
       
       

    return render(request,"post.html")


def reply_view(request):
    try:
        data = json.loads(request.body)
        cmtID = data['commentID']
        comment = Comment.objects.get(id=cmtID)
        username = request.user.username
        user = CustomBlogUser.objects.get(username=username)
        reply = data['comment']

        if reply and user and comment:
            newReply = Reply(
                comment=comment,
                user=user,
                reply=reply
            )
            newReply.save()
            return HttpResponse(status=200)
        return HttpResponse(status=404)
    except Exception as e:
        print(e)
        return HttpResponse(status=504)
