from django.urls import path
from  . import views 

urlpatterns = [

# from tour app
    path("",views.index),
    path("index",views.index,name="index"),
    path("book",views.book,name="book"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("package", views.package, name="package"),
    path("add", views.add, name="add"),
    path("book", views.book, name="book"),

    
#from account app
  
]
