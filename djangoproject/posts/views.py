from django.shortcuts import render
from django.http import HttpResponseRedirect
from posts.forms import HomeForm
from django.views.generic import TemplateView


#Q 1: use TemplateView?
#Q 2: html form or django form?
    #NOTe when using django validation make them read the 
    #documentation to check it is entirely approorpaite for the context

class HomeView(TemplateView):
    template_name = 'posts/index.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            form = HomeForm()
        
        return render(request, self.template_name, {'form': form})


