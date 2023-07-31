from django.shortcuts import render
from django.http import HttpResponse

def friends_view(request):
    return render(request, 'mobilidade/templates/page.html')

# Create your views here.
