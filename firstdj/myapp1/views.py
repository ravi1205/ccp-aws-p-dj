from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi(request):
    return HttpResponse('<h1> THIS IS FROM MYAPP VIEW>PY </h1>')
    return render (request, 'myapp1/hi.html')