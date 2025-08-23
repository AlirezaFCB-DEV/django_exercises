from django.shortcuts import render

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
    if req.method == "POST" :
        form = Add_Post(req.POST)
        if form.is_valid() :
            title = form.cleaned_data["title"]
            post_url = form.cleaned_data["post"]
            content = form.cleaned_data["content"]
            
    else :
        form = Add_Post()
        
    return render(req , "blog/add_post_form.html")