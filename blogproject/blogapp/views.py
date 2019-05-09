from django.shortcuts import render, redirect ,get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blog = Blog.objects
    return render(request,'home.html',{'blogs':blog})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def createBlog(request):
    return render(request,'createBlog.html')

def create(request):
    new_post = Blog()
    new_post.title = request.POST['title']
    new_post.sub_title = request.POST['sub_title']
    new_post.body = request.POST['content']
    new_post.save()
    return redirect('/blog')