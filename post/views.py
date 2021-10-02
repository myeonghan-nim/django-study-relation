from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.


def index(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'post/index.html', context)


def create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('post:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'post/forms.html', context)


def like(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if post.like_users.filter(user=user):
        post.like_users.remove(user)
    else:
        post.like_users.add(user)

    return redirect('post:index')
