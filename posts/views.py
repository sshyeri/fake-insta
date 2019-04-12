from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
    context = {
        'post_form' : post_form,
    }
    return render(request, 'posts/form.html', context)
    
def list(request):
    posts = get_list_or_404(Post.objects.order_by('-pk'))
    context = {'posts': posts}
    return render(request, 'posts/list.html', context)
    
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    context = {'post_form': post_form}
    return render(request, 'posts/form.html', context)
    
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if reqeust.method =='POST':
        post.delete()
    return redirect('posts:list')