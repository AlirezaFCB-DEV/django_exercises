from django.shortcuts import render

from .models import Post
# Create your views here.


def post_list(req):
    posts = Post.objects.all()

    return render(req, "blog/all_posts.html", {"posts": posts})


def post_detail(req, post_url):
    try:
        post = Post.objects.get(post_url=post_url)

        return render(req, "blog/post.html", {"post": post})

    except Post.DoesNotExist:
        return render(req, "blog/404.html",  status=404)
