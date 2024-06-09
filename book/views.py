from django.shortcuts import render,redirect
from .forms  import *
from .models import *
from django.forms import inlineformset_factory
from .filters import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def dashboard(request):
    orders=Order.objects.all()
    customers=CUSTOMER.objects.all()
    context={
        "orders":orders,
        "customers":customers
    }
    return render(request, 'book/dashboard.html',context)
def custamer(request,pk):
    customer=CUSTOMER.objects.get(id=pk)
    orders=customer.order_set.all()
    searchFilter=orderFilters(request.GET,queryset=orders)
    orders=searchFilter.qs
    
    context={
        'customer':customer,
        'orders':orders,
        'searchFilter':searchFilter
    }
    return render(request, 'book/customer.html',context)
def book(request):
    book=BOOK.objects.all()
    return render(request, 'book/book.html',{"book":book})
def create(request):
    form=OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        "form":form,
        }
    return render(request,'book/ordersForm.html' , context)
def update(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        "form":form,
        }
    return render(request,'book/ordersForm.html' , context)

def delete(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context={
        'order':order
    }
    return render(request,'book/deleteOrder.html',context)





def createOrders(request, pk):
    OrderFormset=inlineformset_factory(CUSTOMER,Order,fields=('book','status','tag'),extra=5)
    customer=CUSTOMER.objects.get(id=pk)
    formset=OrderFormset(queryset=Order.objects.none(),instance=customer)
    if request.method=='POST':
        formset=OrderFormset(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={
        'formset':formset
    }
    return render(request,"book/createOrder.html", context)



def register(request):
    form=createNewUser()
    if request.method=='POST':
        form=createNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        'form':form
    }
    return render(request,'book/register.html',context)
def userLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else :
            messages.info(request,'error')
    return render(request,'book/login.html')

            
        