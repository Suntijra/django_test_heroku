from  django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
from djangoheroku import settings
def form(request):
    return HttpResponse(f'{Path(__file__).resolve().parent.parent}')
def index(request):
    return render(request, 'index.html')
def test(request):
    return render(request,'test.html')
def testInclude(request):
    return render(request,'index_test_include.html')
def static_media(request):
    return render(request,'statics//static-media.html')
def static_css(request):
    return render(request,'statics//static-css.html')
def static_js(request):
    return render(request,'statics//static-js.html')