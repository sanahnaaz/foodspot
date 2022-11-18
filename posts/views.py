import datetime as DT

from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from main.functions import generate_form_errors
from posts.forms import FoodForm
from posts.models import Students,SelectedFood


# @login_required(login_url="/users/login/")
# def create_post(request):
#     context = {
#         "title": "Create Student"
#     }
#     return render(request, "posts/order.html", context=context)


@login_required(login_url="/users/login/")
def order(request):
    today = DT.date.today()
    day_one = today + DT.timedelta(days=1)
    day_two = today + DT.timedelta(days=2)
    day_three = today + DT.timedelta(days=3)
    day_four = today + DT.timedelta(days=4)
    day_five = today + DT.timedelta(days=5)
    day_six = today + DT.timedelta(days=6)
    day_seven = today + DT.timedelta(days=7)
    
    dates = [day_one,day_two,day_three,day_four,day_five,day_six,day_seven]
    print(dates)
    
    if request.method == "POST":
        form = FoodForm(request.POST)
        user = request.user
        if form.is_valid():
            print("valid--------------------")
            print(form.cleaned_data)
            instance = form.save(commit=False)
            instance.date1 = day_one
            instance.date2 = day_two
            instance.date3 = day_three
            instance.date4 = day_four
            instance.date5 = day_five
            instance.date6 = day_six
            instance.date7 = day_seven

            student = Students.objects.get(user=user)
            if SelectedFood.objects.filter(student=student):
                context = {
                    'title': "Home",
                    'message': "Already ordered"
                }
                return render(request, 'posts/order.html', context)
            else:
                instance.student = Students.objects.get(user=user)
                instance.save()

                return HttpResponseRedirect(reverse('web:index'))
        else:
            message = generate_form_errors(form)
            context = {
                'title': "Order",
                'dates':dates,
                'form': form,
                'errors': message
            }
            return render(request, 'posts/order.html', context)
            
        context = {
            'title': "Order",
            'dates':dates,
            'form': form
        }
        return render(request, 'posts/order.html', context)
    
    else:
        form = FoodForm()
        context = {
            'title': "Order",
            'dates':dates,
            'form': form
        }
        return render(request, 'posts/order.html', context)
