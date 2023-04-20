from django.contrib import messages
from django.shortcuts import *
from django.views import View
from .models import *
from Merchant.models import *


# Create your views here.

def user_login(request):
    return render(request, 'customer/user_login.html')


def add_user(request):
    name = request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    password = request.POST['password']
    dob = request.POST['dob']
    address = request.POST['address']
    city = request.POST['city']

    user = Client(name=name, email=email, mobile=mobile, password=password, dob=dob, address=address,
                  city=city)
    user.save()
    messages.warning(request, name + 'Has been registered. Please login now...')
    return redirect('user_login')


def login(request):
        email = request.POST['email']
        password = request.POST['password']
        userlogin = Client.objects.filter(email=email, password=password)
        if len(userlogin) == 0:
            messages.warning(request, "Invalid Username Or Password")
        else:
            messages.success(request, "Login Successful!")
            d = {
                'id': userlogin[0].id,
                'email': email,
                'name': userlogin[0].name,
                'mobile': userlogin[0].mobile
            }
            request.session['user'] = d
        return redirect('user_login')


def user_logout(request):
    del request.session['user']
    messages.success(request, 'User has been logged out')
    return redirect('user_login')


def index(request):
    return render(request, 'customer/index.html')


def view(request):
    prod = Products.objects.all()
    cat = Category.objects.all()
    return render(request, 'customer/view.html', {'prod': prod, 'cat': cat})


def viewProductByCategory(request, id):
    prod = Products.objects.filter(category_id=id)
    cat = Category.objects.all()
    return render(request, 'customer/view.html', {'prod': prod, 'cat': cat})


def searchproducts(request):
    search = request.GET['search']
    cat = Category.objects.all()
    prod = Products.objects.filter(name__contains=search)

    return render(request, 'customer/view.html', {'prod': prod, 'cat': cat})


def productdetails(request, id):
    obj = Products.objects.get(id=id)
    cat = Category.objects.get(id=id)
    return render(request, 'customer/productdetails.html', {'obj': obj, 'cat': cat})


def saveProductToCart(request):
    productID = request.POST['productID']
    quantity = int(request.POST['quantity'])
    customers_id = request.session['user']['id']
    prod_obj = Products.objects.get(id=productID)
    total_price = float(prod_obj.price) * quantity

    cartobj = Cart()
    cartobj.product_id = productID
    cartobj.quantity = quantity
    cartobj.client_id = customers_id
    cartobj.total_price = total_price
    cartobj.save()

    return render(request, 'customer/shopping_cart.html')
