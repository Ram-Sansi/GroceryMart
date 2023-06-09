from django.urls import path
from .views import *

urlpatterns = [

    path("merchant_login", merchant_login, name="merchant_login"),
    path("register_merchant", register_merchant, name="register_merchant"),
    path("login", login, name="login"),
    path("merchant_logout", merchant_logout, name='merchant_logout'),
    path("contact_us", contact_us, name='contact_us'),
    path("about_us", about_us, name='about_us'),
    path("profile", profile, name='profile'),
    path("changeMerchantPassword", changeMerchantPassword, name='changeMerchantPassword'),
    path("updateprofile", updateprofile, name='updateprofile'),

    # category url
    path("addcategory", category.as_view(), name="addcategory"),
    path("viewcategory", viewcategory, name="viewcategory"),

    # products url

    path("products", products.as_view(), name="products"),
    path("viewproducts", viewProducts, name='viewproducts'),
    path("update_product/<int:prodid>", update_product, name='update_product'),
    path("delete_product/<int:id>", delete_product, name='delete_product'),
    path("saveupdate/<int:id>", saveupdate, name='saveupdate'),
    path("saveupdate/<int:id>", saveupdate, name='saveupdate'),
    path("userproduct", userproduct, name='userproduct'),

]
