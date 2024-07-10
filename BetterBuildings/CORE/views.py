from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReportingForm


#page requests
def home(request):
    return render(request,"index.html")

def reporting(request):
    return render(request, "reporting.html")

def display(request):
    return render(request, "display.html")

def reportPosted(request):
    return render(request, "reportPosted.html")


#form requests 
def report(request):
    if request.method == "POST":
        form = ReportingForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/reports/")
        else:
            form = ReportingForm()
        return render(request, "reporting.html", {"form": form})
        

