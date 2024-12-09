from django.shortcuts import HttpResponse, render

def mainpage(request):
    return render(request, 'account/mainpage.html')
