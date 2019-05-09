from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('blog/<int:blog_id>',views.detail,name='detail'),
    path('create',views.create,name='create'),
    path('createBlog',views.createBlog,name='createBlog'),
]
