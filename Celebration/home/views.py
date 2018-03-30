from django.shortcuts import render, render_to_response
from django.template.context_processors import request

# Create your views here.
def index(request):
    return render_to_response('static/index.html')