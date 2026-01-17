from django.shortcuts import render,redirect
from posts.models import Post , Likepost
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required

# @login_required
def home(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # must include request.FILES
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/')  # redirect to posts page
    else:
        form = PostForm()

    return render(request, 'createpost.html', {'form': form})



def likepost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')


    post = Post.objects.get(id=post_id)
    like_filter = Likepost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = Likepost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.like=post.like+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.like=post.like-1
        post.save()
        return redirect('/')
