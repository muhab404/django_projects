from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from .decorators import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
            
            # another creation of user customer without signals
			# group = Group.objects.get(name='customer')
			# user.groups.add(group)
			# #Added username after video because of error returning customer name if not added
			# Customer.objects.create(
			# 	user=user,
			# 	name=user.username,
			# 	)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'register.html', context)
            

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

        
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def dashboard(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	orders = request.user.customer.order_set.all()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	print('ORDERS:', orders)

	context = {'orders':orders, 'total_orders':total_orders,
	'delivered':delivered,'pending':pending}
	return render(request, 'user.html', context)  

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def products(request):
    products=Product.objects.all()
    context={
        'products':products
    }

    return render(request,'products.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    myFilter = OrderFilter(request.GET , queryset= orders)
    orders=myFilter.qs
	
    order_count = orders.count()
    context = {'customer':customer, 'orders':orders, 'order_count':order_count ,
    'myfilter':myFilter}

    return render(request,'customer.html',context)  

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def createOrder(request):
    form=OrderForm()

    if request.method== 'POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form

    }          
    return render(request,'order_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form=OrderForm(instance= order)

    if request.method== 'POST':
        form=OrderForm(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form

    }          
    return render(request,'order_form.html',context)    


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    

    if request.method== 'POST':

        order.delete()   
        return redirect('/')

    context={
        'item':order}          
    return render(request,'delete.html',context)        