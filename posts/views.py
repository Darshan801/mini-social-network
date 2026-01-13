from django.shortcuts import render,redirect
from posts.models import Post
from posts.forms import PostForm

def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # must include request.FILES
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/post')  # redirect to posts page
    else:
        form = PostForm()

    return render(request, 'createpost.html', {'form': form})
