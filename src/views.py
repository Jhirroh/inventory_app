from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Customer, Product, Order
from .forms import OrderForm, ProductForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='login')
@admin_only
def dashboardPage(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    orderCount = orders.count()
    deliveredCount = orders.filter(status='Delivered').count()
    pendingCount = orders.filter(status='Pending').count()
    outOfDeliveryCount = orders.filter(status='Out of Delivery').count()

    context = { 'orders': orders, 'customers': customers,
    'orderCount': orderCount, 'deliveredCount': deliveredCount, 
    'pendingCount': pendingCount, 'outOfDeliveryCount': outOfDeliveryCount}

    return render(request, 'admin/dashboard.html', context)

@login_required(login_url='login')
@admin_only
def productPage(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'admin/product.html', context)

@login_required(login_url='login')
@admin_only
def orderDetails(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'admin/detail.html', context)

@login_required(login_url='login')
@admin_only
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'admin/detail.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customerPage(request, pk): 
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    context = {'orders': orders}
    return render(request, 'admin/customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()

    context = {'orders': orders}
    return render(request, 'customer/user.html', context)

'''
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userOrderPage(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(instance=customer)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('user')
    context = {'form': form}
    return render(request, 'customer/order_detail.html', context)
'''