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


def contact_us(request):
    return render(request, 'customer/contact_us.html')


def about_us(request):
    return render(request, 'customer/about_us.html')


def wishlist(request):
    return render(request, 'customer/wishlist.html')


def checkout(request):
    return render(request, 'customer/checkout.html')


def shopping_cart(request):
    return render(request, 'customer/shopping_cart.html')


def add_to_cart(request):
    cart = Cart.objects.filter(client_id=request.session['user']['id'])
    total = 0
    for items in cart:
        total += float(items.total_price)
    return render(request, 'customer/shopping_cart.html', {'cart': cart, 'total': total})


@csrf_exempt
def changecart_quantity(request, id):
    New_quantity = float(request.POST["quantity"])
    cartobj = Cart.objects.get(id=id)
    cartobj.quantity = float(New_quantity)
    ppi = cartobj.Products.price

    cartobj.total_price = New_quantity * ppi
    cartobj.save()
    return HttpResponse('success')


def delete_cart(request, id):
    prod = Cart.objects.get(id=id)
    prod.delete()
    return redirect('add_to_cart')
