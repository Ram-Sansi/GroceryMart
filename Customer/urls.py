from django.urls import path
from .views import *

urlpatterns = [

    # user urls

    # path("", index, name="index"),
    path("user_login", user_login, name="user_login"),
    path("add_user", add_user, name="add_user"),
    path("login", login, name="login"),
    path("user_logout", user_logout, name="user_logout"),
    path("", view, name="view"),
    path("viewProductByCategory/<int:id>", viewProductByCategory, name="viewProductByCategory"),
    path("searchproducts", searchproducts, name="searchproducts"),
    path("productdetails/<int:id>", productdetails, name="productdetails"),
    path("saveProductToCart", saveProductToCart, name="saveProductToCart"),
    path("contact_us", contact_us, name="contact_us"),
    path("about_us", about_us, name="about_us"),
    path("wishlist/<int:id>", wishlist, name="wishlist"),
    path("shopping_cart/<int:id>", shopping_cart, name="shopping_cart"),
    path("add_to_cart", add_to_cart, name="add_to_cart"),
    path("changecart_quantity/<int:id>", changecart_quantity, name='changecart_quantity'),
    path("delete_cart/<int:id>", delete_cart, name='delete_cart'),
    path("ConfirmOrder", ConfirmOrder, name="ConfirmOrder"),
    path("dashboard", dashboard, name="dashboard"),
    path("billdetails/<int:id>", billdetails, name="billdetails"),
    path("updateprofile", updateprofile, name="updateprofile"),
    path("changeClientPassword", changeClientPassword, name="changeClientPassword"),

]
