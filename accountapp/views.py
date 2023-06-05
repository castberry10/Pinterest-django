from django.shortcuts import render
from accountapp.models import HelloWorld
# from django.http import HttpResponse

# Create your views here.


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')  # 리퀘스트에서 Post 중에서 hello_world_input라는 데이터를 가져와라..
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        return render(request, 'accountapp/helloworld.html', context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/helloworld.html', context={'text': 'GET METHOD!'})

