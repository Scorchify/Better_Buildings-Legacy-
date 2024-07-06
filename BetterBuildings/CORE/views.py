from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def reporting(request):
    return render(request, "reporting.html")

def display(request):
    return render(request, "display.html")
