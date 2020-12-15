from itertools import chain
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import auth
from django.contrib.messages import error
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def login(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            cleandatas = form.cleaned_data
            username = cleandatas['username']
            password = cleandatas['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_driver:
                    auth.login(request, user)
                    return render(request, 'driver_portal.html')
                elif user.is_owner:
                    auth.login(request, user)
                    return render(request, 'owner_portal.html')
                else:
                    return render(request, 'login.html')
            else:
                error(request, "Wrong username or password ")
                return redirect('/')
        return render(request, 'login.html', {'form': form})
    else:
        form = Loginform()
        return render(request, 'login.html', {'form': form})


def owner_registration(request):
    if request.method == "POST":
        form = Owner_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login)
        return render(request, 'owner_registration.html', {'form': form})
    else:
        form = Owner_registration_form()
        return render(request, 'owner_registration.html', {'form': form})

@login_required(login_url='/')
def driver_recieve_portal(request):
    if request.method == "POST":
        form = Driver_recieve_portal_form(request.POST)
        if form.is_valid():
            form.save()
            data = Driver_recieve_portal.objects.last()
            data.vehicle=Vehicle.objects.get(driver=User.objects.get(username=request.user.username))
            data.vehicle = Vehicle.objects.get(driver=User.objects.get(username=request.user.username))
            data.save()
            return redirect(driver_recieve_portal)
        return render(request, 'driver_recieve_portal.html', {'form': form})
    else:
        form = Driver_recieve_portal_form()
        return render(request, 'driver_recieve_portal.html', {'form': form})


@login_required(login_url='/')
def driver_pay_portal(request):
    if request.method == "POST":
        form = Driver_pay_portal_form(request.POST)
        if form.is_valid():
            form.save()
            data = Driver_pay_portal.objects.last()
            data.vehicle = Vehicle.objects.get(driver=User.objects.get(username=request.user.username))
            my_user = User.objects.get(username=request.user.username)
            data.vehicle = Vehicle.objects.get(driver=my_user)
            data.save()
        return redirect(driver_pay_portal)
    else:
        form = Driver_pay_portal_form()
        return render(request, 'driver_pay_portal.html', {'form': form})




@login_required(login_url='/')
def add_vehicle(request):
    if request.method == "POST":
        form1 = Add_vehicle_form(request.POST)
        form2 = Driver_registration_form(request.POST)
        if form1.is_valid and form2.is_valid():
            form1.save()
            form2.save()
            driver_username = form2.cleaned_data['username']
            data = Vehicle.objects.last()
            data.username = User.objects.get(username=request.user.username)
            data.driver = User.objects.get(username=driver_username)
            data.save()
            return render(request, 'owner_portal.html')
        else:
            return render(request, 'add_vehicle.html', {'form1': form1, 'form2': form2})
    else:
        user_have_vehicles = Vehicle.objects.filter(username=User.objects.get(username=request.user.username)).count()
        if request.user.no_of_vehicles > user_have_vehicles:
            form1 = Add_vehicle_form()
            form2 = Driver_registration_form()
            return render(request, 'add_vehicle.html', {'form1': form1, 'form2': form2})
        else:
            return render(request, 'vehicle_max.html')


@login_required(login_url='/')
def my_vehicle(request):
    vehicles = Vehicle.objects.filter(username=User.objects.get(username=request.user.username))
    return render(request, 'my_vehicle.html', {'vehicles': vehicles})


@login_required(login_url='/')
def vehicle_portal(request, id=id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request, 'vehicle_portal.html', {'id': id, 'vehicle': vehicle})


@login_required(login_url='/')
def view_statement(request, id):
    from_date = timezone.now()
    to_date = timezone.now()
    if request.method == "POST":
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
    pay_data = Driver_pay_portal.objects.filter(vehicle=Vehicle.objects.get(id=id))
    recieve_data = Driver_recieve_portal.objects.filter(vehicle=Vehicle.objects.get(id=id))
    comment_data = Comment.objects.filter(vehicle=Vehicle.objects.get(id=id))
    pay_data2 = pay_data.filter(date__range=[from_date, to_date]).values_list('date',
                                                                              flat=True).distinct()
    recieve_data2 = recieve_data.filter(date__range=[from_date, to_date]).values_list('date',
                                                                                      flat=True).distinct()
    comments2 = comment_data.filter(date__range=[from_date, to_date]).values_list('date',
                                                                                  flat=True).distinct()
    dates_list = list(chain(pay_data2, recieve_data2, comments2))
    dates = dict.fromkeys(dates_list)
    return render(request, 'statement.html',
                  {'pay_data': pay_data, 'recieve_data': recieve_data, 'dates': dates, 'comments': comment_data,
                   'id': id})

@login_required(login_url='/')
def view_statement(request, id):
    from_date = timezone.now()
    to_date = timezone.now()
    if request.method == "POST":
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
    pay_data = Driver_pay_portal.objects.filter(vehicle=Vehicle.objects.get(id=id))
    recieve_data = Driver_recieve_portal.objects.filter(vehicle=Vehicle.objects.get(id=id))
    comment_data = Comment.objects.filter(vehicle=Vehicle.objects.get(id=id))
    pay_data2 = pay_data.filter(date__range=[from_date, to_date]).values_list('date',
                                                                              flat=True).distinct()
    recieve_data2 = recieve_data.filter(date__range=[from_date, to_date]).values_list('date',
                                                                                      flat=True).distinct()
    comments2 = comment_data.filter(date__range=[from_date, to_date]).values_list('date',
                                                                                  flat=True).distinct()
    dates_list = list(chain(pay_data2, recieve_data2, comments2))
    dates = dict.fromkeys(dates_list)
    return render(request, 'statement.html',
                  {'pay_data': pay_data, 'recieve_data': recieve_data, 'dates': dates, 'comments': comment_data,
                   'id': id})


def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        if check_password(old_password, request.user.password):
            password = make_password(new_password)
            myuser = request.user
            myuser.password = password
            myuser.save()
            return HttpResponse("changed")
        else:
            return HttpResponse('not_valid')
    else:
        return HttpResponse("not post")


@login_required(login_url='/')
def comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            data = Comment.objects.last()
            data.username = Vehicle.objects.get(driver=User.objects.get(username=request.user.username))
            data.save()
            return render(request, 'driver_portal.html')
    else:
        form = CommentForm()
        return render(request, 'comment.html', {'form': form})

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')


def username_checker(request):
    username = request.POST.get('username')
    all_users = User.objects.values_list('username', flat=True)
    if username in all_users:
        return HttpResponse("not_valid")
    else:
        return HttpResponse("valid")
