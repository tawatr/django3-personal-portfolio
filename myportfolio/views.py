from django.shortcuts import render

from .models import myProject
# Create your views here.
def home(request):
    # import all attributes of model
    # and turn to python object
    proj = myProject.objects.all()
    return render(request,'myportfolio/home.html',
    {'proj':proj})
