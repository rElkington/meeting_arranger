from django.shortcuts import render
from django.http import HttpResponseRedirect
from posts.forms import HomeForm


#Q 1: use TemplateView?
#Q 2: html form or django form?
    #NOTe when using django validation make them read the 
    #documentation to check it is entirely approorpaite for the context

def index(request):
    if request.method == 'POST':
        f = HomeForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/thanks/')
    else:
        f = HomeForm()
    return render(request, 'posts/index.html', {'form': f})

