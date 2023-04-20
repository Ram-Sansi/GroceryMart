from django.urls import path
from .views import *

urlpatterns = [

    # user urls

    path("", index, name="index"),
    path("user_login", user_login, name="user_login"),
    path("add_user", add_user, name="add_user"),
    path("login", login, name="login"),
    path("user_logout", user_logout, name="user_logout"),
    path("view", view, name="view"),
    path("viewProductByCategory/<int:id>", viewProductByCategory, name="viewProductByCategory"),
    path("searchproducts", searchproducts, name="searchproducts"),
    path("productdetails/<int:id>", productdetails, name="productdetails"),
    path("saveProductToCart", saveProductToCart, name="saveProductToCart"),
]
