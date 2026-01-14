from django.http import HttpResponse
 # include Like if it exists

def friends_home(request):
    return HttpResponse("<h1>Friends Home Page</h1>")

