from django.shortcuts import render

def website(request):
    return render(request, "index.html")
