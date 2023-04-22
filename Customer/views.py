import datetime

from django.contrib import messages
from django.shortcuts import *
from django.views import View
from .models import *
from Merchant.models import *
from Customer.models import *
from django.views.decorators.csrf import csrf_exempt


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
    return redirect('view')


def user_logout(request):
    del request.session['user']
    messages.success(request, 'User has been logged out')
    return redirect('user_login')


# def index(request):
#     return render(request, 'customer/index.html')


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
    customersid = request.session['user']['id']
    prodobj = Products.objects.get(id=productID)
    totalprice = float(prodobj.price) * quantity

    cartobj = Cart()
    cartobj.product_id = productID
    cartobj.quantity = quantity
    cartobj.client_id = customersid
    cartobj.total_price = totalprice
    cartobj.save()

    return redirect('add_to_cart')


def contact_us(request):
    return render(request, 'customer/contact_us.html')


def about_us(request):
    return render(request, 'customer/about_us.html')


def wishlist(request):
    return render(request, 'customer/wishlist.html')


def shopping_cart(request):
    return render(request, 'customer/shopping_cart.html')


def add_to_cart(request):
    show = Cart.objects.filter(client_id=request.session['user']['id'])
    total = 0
    for items in show:
        total += float(items.total_price)
    return render(request, 'customer/shopping_cart.html', {'show': show, 'total': total})


@csrf_exempt
def changecart_quantity(request, id):
    newquantity = float(request.POST['quantity'])
    cartobj = Cart.objects.get(id=id)
    cartobj.quantity = float(newquantity)
    ppi = cartobj.product.price

    cartobj.total_price = (newquantity * ppi)
    cartobj.save()
    return HttpResponse('success')


def delete_cart(request, id):
    prod = Cart.objects.get(id=id)
    prod.delete()
    return redirect('add_to_cart')


def ConfirmOrder(request):
    customerId = request.session['user']['id']
    cartItems = Cart.objects.filter(client_id=customerId)
    totalCost = 0
    totalItems = 0
    for items in cartItems:
        totalItems += float(items.quantity)
        totalCost += float(items.total_price)

    # BILL LOGIC STARTS_____________
    billObj = Bill()
    billObj.Client_id = customerId
    billObj.totalprice = totalCost
    billObj.totalitems = totalItems
    billObj.billdate = datetime.date.today()
    billObj.billtime = datetime.datetime.now().time()
    billObj.save()
    # BILL LOGIC COMPLETED ___ BILL DETAILS START ___

    billId = billObj.id

    for items in cartItems:
        # new obj in every iteration
        billDetailObj = Billdetail()
        billDetailObj.Bill_id = billId
        billDetailObj.Client_id = customerId
        billDetailObj.Product_id = items.product_id
        billDetailObj.quantity = items.quantity
        billDetailObj.itemprice = items.total_price
        billDetailObj.save()
        items.delete()

    return render(request, 'customer/placeorder.html')


def dashboard(request):
    return render(request, 'customer/dashboard.html')


def viewbill(request, id):
    bill = Bill.objects.get(id=id)
    billdetail = Billdetail.objects.get(id=id)

    return render(request, 'customer/dashboard.html', {'bill': bill, 'billdetail': billdetail})
