from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()


class BlogComment(models.Model):
    content = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)


def __str__(self):
    return self.title
