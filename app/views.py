from django.shortcuts import render
from app.models import Post
import datetime
# Create your views here. 

 

def home(request):
    
    posts = Post.objects.all() 
    
     
    return render(request,'index.html',{'posts':posts})

def upload_video(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post.html',{'post':post})