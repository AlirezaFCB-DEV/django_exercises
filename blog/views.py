from django.shortcuts import render, redirect
from django.utils.text import slugify

from datetime import datetime

from .models import Post
from .forms import Add_Post
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


def add_post(req):
    if req.method == "POST":
        form = Add_Post(req.POST)
        if form.is_valid():

            data = form.cleaned_data
            slug_str = data["post_url"] or slugify(
                data["title"]),

            Post.objects.create(title=data["title"],
                                post_url= slug_str,content=data["content"],
                                published_date=datetime.now())

            return redirect("post_list")
    else:
        form = Add_Post()

    return render(req, "blog/add_post_form.html", {"form": form})
