from django.shortcuts import render

# Create your views here.

def index(request):
    return "Hello world"# return render(request, 'shop/index.html', context=context)