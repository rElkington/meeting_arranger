from django.shortcuts import render
from django.http import HttpResponseRedirect
from posts.forms import HomeForm, PostModelForm

#Q 1: use TemplateView?
#Q 2: html form or django form?
    #NOTe when using django validation make them read the 
    #documentation to check it is entirely approorpaite for the context

def index(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            lect_name = form.cleaned_data['slect_name']
            time = form.cleaned_data['time']
            date = form.cleaned_data['m_date']
            descript = form.cleaned_data['descript']
            return HttpResponseRedirect('/thanks/')
    else:
        form = HomeForm()
    return render(request, 'posts/index.html', {'form': form})

def PostFormDetail(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = HomeForm()
    return render(request, 'posts/index.html', {'form': form})
