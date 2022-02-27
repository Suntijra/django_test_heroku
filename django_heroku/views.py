from  django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
def form(request):
    return HttpResponse(f'{Path(__file__).resolve().parent.parent}')
def index(request):
    return render(request, 'index.html')