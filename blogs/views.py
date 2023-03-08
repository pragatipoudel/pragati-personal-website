from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

def index(request):
    posts = Post.objects.all()
    return render(request, 'blogs/index.html', {
        'posts': posts
    })

def detail(request, blog_id):
    post = get_object_or_404(Post, id=blog_id)
    return render(request, 'blogs/detail.html', {
        'post': post
    })

def comment(request, blog_id):
    post = get_object_or_404(Post, id=blog_id)
    message = request.POST['message']
    user = request.POST['user']
    comment = Comment(
        message = message,
        comment_user = user,
        post = post
    )
    comment.save()
    return redirect('blogs:detail', blog_id=post.id)


