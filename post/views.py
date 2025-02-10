from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# Барлық посттарды шығару
def post_list(request):
    posts = Post.objects.all()
    return JsonResponse({'posts': list(posts.values())})

# Белгілі бір постты шығару
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return JsonResponse({'title': post.title, 'description': post.description, 'author': post.author})

# Жаңа пост қосу
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})

# Постты жою
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')
