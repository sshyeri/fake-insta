from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import PostForm, ImageForm, CommentForm
from .models import Post, Image
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False) #게시글 내용 처리 끝
            post.user = request.user
            post.save()
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
                    
            return redirect('posts:list')
    else:
        post_form = PostForm()
        image_form = ImageForm()
    context = {
        'post_form' : post_form,
        'image_form' : image_form,
    }
    return render(request, 'posts/form.html', context)
    
def list(request):
    posts = get_list_or_404(Post.objects.order_by('-pk'))
    form = CommentForm()
    context = {'posts': posts,
                'form': form,
    }
    
    return render(request, 'posts/list.html', context)

@login_required    
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.user != request.user:
        return redirect('posts:list')
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    context = {'post_form': post_form}
    return render(request, 'posts/form.html', context)

@login_required    
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.user != request.user:
        return redirect('posts:list')
    if request.method =='POST':
        post.delete()
    return redirect('posts:list')