from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from accountapp.models import HelloWorld
from django.urls import reverse
# from django.http import HttpResponse

# Create your views here.


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')  # 리퀘스트에서 Post 중에서 hello_world_input라는 데이터를 가져와라..

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        return HttpResponseRedirect(reverse('accountapp:hello_world')) #accountapp에 있는 hello_world로 가달라
    else:

        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'hello_world_list': hello_world_list})

