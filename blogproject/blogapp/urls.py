from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('blog/<int:blog_id>',views.detail,name='detail'),
    path('edit/<int:blog_id>',views.edit,name="edit"),
    path('createBlog',views.createBlog,name='createBlog'),
    path('create',views.create,name='create'),
    path('update/<int:blog_id>',views.update,name="update"),
    path('delete/<int:blog_id>',views.delete,name="delete"),
    path('commentcreate/<int:blog_id>',views.commentcreate,name="commentcreate"),
    path('commentdelete/<int:blog_id>/<int:comment_id>',views.commentdelete,name="commentdelete"),
    
]
   
    
    
   
    
    
    