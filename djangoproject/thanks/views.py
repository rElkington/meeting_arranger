from django.shortcuts import render
from django.http import HttpResponse
import textwrap

def indexThanks(request):
    return render(request, 'thanks/index.html')