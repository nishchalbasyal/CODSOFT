from django.urls import path
from .views import *;

urlpatterns = [
    path('', home,name="home"),
    path('login', LoginViewUser.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('register', register,name="register"),
    path('write', Add_Post.as_view(),name="post.new"),
    path('<str:slug>/update', Update_View.as_view(),name="post.update"),
    path('delete/<str:slug>', delete_view, name="delete.url"),
    path('<str:slug>', single_post,name="singlePost"),
    path('<str:slug>/comment', comment,name="comment_form"),
    path('post/comment/reply', reply_view,name="comment_form"),
    path('author/<username>', author_view,name="author.url"),
    path('search/results/all/', search_view, name="search.url"),
]
