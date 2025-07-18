from django.shortcuts import render, HttpResponse, redirect
from posts.models import Post
from posts.forms import PostForm, CreateForm

# Create your views here.

def home(request):
    return render(request, "base.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    post = Post.objects.filter(id = post_id).first()
    return render(request, "posts/post_detail.html", context={"post": post})

# Вариант №1
# def post_create_view(request):
#     if request.method == "GET":
#         form = PostForm()
#         return render(request, "posts/post_create.html", context={"form":form})
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if not form.is_valid():
#             return render(request, "posts/post_create.html", context={"form":form})
#         image = form.cleaned_data.get("image")
#         title = form.cleaned_data.get("title")
#         content = form.cleaned_data.get("content")
#         Post.objects.create(title=title, content=content, image=image)
#         return redirect("/posts")
    
# Вариант №1    
def created_post(request):
    if request.method == "GET":
        form = CreateForm()
        return render(request, "posts/post_create.html", context={"form":form})
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form":form})
        image = form.cleaned_data.get("image")
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        Post.objects.create(title=title, content=content, image=image)
        return redirect("/posts")