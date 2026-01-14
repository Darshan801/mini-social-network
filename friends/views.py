from django.http import HttpResponse
 # include Like if it exists

##def friends_home(request):
    #return HttpResponse("<h1>Friends Home Page</h1>")

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import FriendRequest

User = get_user_model()   # ✅ THIS IS THE KEY LINE


@login_required
def friends_list(request):
    users = User.objects.exclude(id=request.user.id)

    sent_requests = FriendRequest.objects.filter(
        from_user=request.user
    ).values_list('to_user_id', flat=True)

    context = {
        'users': users,
        'sent_requests': sent_requests,
    }
    return render(request, 'friends/friends_list.html', context)


@login_required
def send_friend_request(request, user_id):
    to_user = User.objects.get(id=user_id)

    FriendRequest.objects.get_or_create(
        from_user=request.user,
        to_user=to_user
    )

    return redirect('friends:list')




User = get_user_model()


@login_required
def friend_requests(request):
    requests = FriendRequest.objects.filter(
        to_user=request.user,
        is_accepted=False
    )
    return render(request, 'friends/requests.html', {'requests': requests})


@login_required
def accept_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest,
        id=request_id,
        to_user=request.user
    )
    friend_request.is_accepted = True
    friend_request.save()
    return redirect('friends:requests')


@login_required
def reject_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest,
        id=request_id,
        to_user=request.user
    )
    friend_request.delete()
    return redirect('friends:requests')