from django.urls import path
from .views import *

urlpatterns =[
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>', DetailCategory.as_view(), name="singlecategory" ),
    
    path('books', ListBook.as_view(), name='books'),
    path('books/<int:pk>', DetailBook.as_view(), name='singlebooks'),
    
    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>', DetailProduct.as_view(), name='singleproducts'),
    
    path('users', ListUsers.as_view(), name='users'),
    path('users/<int:pk>', DetailUser.as_view(), name='singleusers'),

    path('carts', ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>', DetailCart.as_view(), name='cartdetails'),
]