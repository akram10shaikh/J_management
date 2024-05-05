from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from myapp.models import Info
from django.db import IntegrityError

# Create your views here.

def base(request):
    u = request.session.get('user_login')
    return render(request, 'base.html', {'u': request.user.username})


def index(request):
    return render(request,'index.html')

def log1(request):
    return render(request,'log1.html')


def second(request):
    return render(request,'second.html')

def add_data(request):
    return render(request,'add_data.html')


def log_out(request):
    logout(request)
    return render(request,'index.html')

def add_user(request):
    return render(request,'add_user.html')

# Add user
def add(request):
    if request.method == 'POST':
        try:
            user = request.POST.get('user')
            password = request.POST.get('password')
            user = User.objects.create_user(username=user,password=password)
            user.save()
            output = 'User is Created now login into the account'
            return render(request, 'add_user.html',{'output':output})

        except IntegrityError:
            output = 'Username is already exist'
            return render(request, 'add_user.html', {'output': output})
    else:
        return render(request,'add_user.html')


#  Login User
def login_page(request):
    if request.method == 'POST':
        user1 = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request,username=user1,password=password)
        if user is not None:
            login(request,user)
            request.session['user_login'] = user1
            request.session.save()
            return render(request,'log1.html')

        else:
            error = 'Invalid User or Password'
            return render(request,'index.html',{'final':error})

# Add Employee
def employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        user = Info.objects.create(name=name,age=age,city=city,phone=phone,department=department,salary=salary)
        user.save()
        msg = 'Data is saved'
        return render(request, 'second.html', {'msg': msg})

# Display Employee

def display(request):
    user2 = Info.objects.all()
    return render(request,'display.html',{'user2':user2})

def display_one(request):
    return render(request,'display_one.html')

def edit(request):
    user2 = Info.objects.all()
    return render(request,'edit.html',{'user2':user2})

# Edit single record

def edit_record(request,id):
    data = Info.objects.get(id=id)
    return render(request,'edit_record.html',{'data':data})

def edit_apply(request):
    try:
        id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        salary = request.POST.get('salary')

        employee = Info.objects.get(id=id)

        employee.name = name
        employee.age = age
        employee.city = city
        employee.phone = phone
        employee.department = department
        employee.salary = salary
        employee.save()
        msg = 'Record successfully updated'
        return render(request, 'edit_record.html', {'msg': msg})
    except Info.DoesNotExist:
        msg = 'Something went wrong'
        return render(request,'edit.html',{'msg':msg})


def search(request):
    return render(request,'search.html')


def search_data(request):
    if request.method == 'POST':
        emp_field = request.POST.get('emp')
        data_to_search = request.POST.get('data')

        # Perform the search based on the selected field
        if emp_field == 'name':
            results = Info.objects.filter(name__icontains=data_to_search)
        elif emp_field == 'age':
            results = Info.objects.filter(age=data_to_search)
        elif emp_field == 'city':
            results = Info.objects.filter(city__icontains=data_to_search)
        elif emp_field == 'phone':
            results = Info.objects.filter(phone=data_to_search)
        elif emp_field == 'department':
            results = Info.objects.filter(department__icontains=data_to_search)
        elif emp_field == 'salary':
            results = Info.objects.filter(salary=data_to_search)
        else:
            results = None

        return render(request, 'search.html', {'results': results})

    return render(request, 'search.html')

def search_page(request):
    return render(request,'search_page.html')


def delete_record(request, id):
    data = get_object_or_404(Info, id=id)

    if request.method == 'POST':
        data.delete()
        msg = 'Record successfully deleted'
        return render(request, 'edit.html', {'msg': msg})

    return render(request, 'delete_record.html', {'data': data})