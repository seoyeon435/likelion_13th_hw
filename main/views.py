from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'main/hw_mainpage.html')

def secondpage(request):
    return render(request, 'main/hw_secondpage.html')