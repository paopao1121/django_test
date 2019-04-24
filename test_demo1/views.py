from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

user_list = [
    {"user":"Jack","pwd":"abc"},
    {"user":"Tom","pwd":"ABC"},
]


def index(request):
    # request.POST
    # request.GET
    #return HttpResponse("hello world!")
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        temp = {"user":username,"pwd":password}
        user_list.append(temp)
        #print(username,password)
    return render(request,"index.html",{"data":user_list})
