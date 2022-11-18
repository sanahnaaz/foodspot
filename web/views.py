from django.shortcuts import render
from django.http.response import HttpResponse

from posts.models import Students,SelectedFood


def index(request):
    
    print(request.user.username)
    if (request.user.username == "admin"):
        students = Students.objects.all()
        context = {
            "title" : "Home Page",
            "students": students
        }
        return render(request, 'web/index.html',context=context)
    else:
        if (request.user.is_authenticated):
            if SelectedFood.objects.filter(student__user = request.user):
                order = SelectedFood.objects.get(student__user = request.user)
                print(order)
                context = {
                    "title" : "Home Page", 
                    "orders":order,           
                }
            else:
                context = {
                    "title" : "Home Page",         
                }
        else:
            context = {
                "title" : "Home Page",        
            }
        return render(request, 'web/index2.html',context=context)