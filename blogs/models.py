from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-pub_date']

class Comment(models.Model):
    message = models.TextField()
    comment_user = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.message} by {self.comment_user}'
    
    class Meta:
        ordering = ['-comment_date']

