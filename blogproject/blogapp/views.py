from django.shortcuts import render, redirect ,get_object_or_404
from .models import Blog,BlogComment

# Create your views here.
def home(request):
    blog = Blog.objects.all()
    return render(request,'home.html',{'blogs':blog})

def createBlog(request):
    return render(request,'createBlog.html')

def create(request):
    new_post = Blog()
    new_post.title = request.POST['title']
    new_post.sub_title = request.POST['sub_title']
    new_post.body = request.POST['content']
    new_post.save()
    return redirect('/blog')

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    comments = blog_detail.blogcomment_set.all()
    
    return render(request,'detail.html',{'blog':blog_detail,'comment':comments})

def edit(req,blog_id):
    one_blog = get_object_or_404(Blog,id=blog_id)
    return render(req,'edit.html',{'blog':one_blog})


def update(req,blog_id):
    if(req.method=='POST'):
        exist_blog = get_object_or_404(Blog,id=blog_id)
        exist_blog.title = req.POST['title']
        exist_blog.body = req.POST['content']
        exist_blog.save()
    return redirect('/blog')

def delete(req,blog_id):
    exist_blog = get_object_or_404(Blog,id=blog_id)
    exist_blog.delete()
    return redirect('/blog')

def commentcreate(req,blog_id):
    if(req.method=='POST'):
        one_blog = get_object_or_404(Blog,id=blog_id)
        one_blog.blogcomment_set.create(content = req.POST['comment'])
    return redirect('/blog/blog/'+str(blog_id))

def commentdelete(req,blog_id,comment_id):
    comments = get_object_or_404(BlogComment,id=comment_id,blog=blog_id)
    comments.delete()
    return redirect('/blog/blog/'+str(blog_id))

