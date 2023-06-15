from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy
# from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from accountapp.forms import AccountUpdateForm
def hello_world(request):
    
    if request.user.is_authenticated:
        pass
    
        if request.method == "POST":
            temp = request.POST.get('hello_world_input')  # 리퀘스트에서 Post 중에서 hello_world_input라는 데이터를 가져와라..

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world')) #accountapp에 있는 hello_world로 가달라
        else:

            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/helloworld.html', context={'hello_world_list': hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html' #회원가입
    
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' 
    template_name = 'accountapp/detail.html'
    
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    
    context_object_name = 'target_user' 
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'
    
    def get(self, *args, **kwargs): #        get_object -> 뷰 안에서 사용되는 pk를 가져옴 request.user> 리퀘스트를 보내고 있는 유저
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            # return HttpResponseRedirect(reverse('accountapp:login'))
            return HttpResponseForbidden()
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()
    
class AccountDeleteView(DeleteView):
    model = User
    
    context_object_name = 'target_user' 
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    
    def get(self, *args, **kwargs): #        get_object -> 뷰 안에서 사용되는 pk를 가져옴 request.user> 리퀘스트를 보내고 있는 유저
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            # return HttpResponseRedirect(reverse('accountapp:login'))
            return HttpResponseForbidden()
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()
    
    