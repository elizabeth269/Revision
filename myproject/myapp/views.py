from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # context = {
    #     'name': "elizabeth",
    #     'age': 23,
    #     'nationality': "nigerian",
    # }
    return render(request, 'index.html')

def counter(request):
    
    return render(request, "counter.html")
