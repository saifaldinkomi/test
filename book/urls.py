from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='home'),
    path('book/',views.book, name='book'),
    path('custamer/<str:pk>',views.custamer,name='customer'),
    path('create/',views.create,name='create'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('createOrders/<str:pk>',views.createOrders,name='createOrders'),
    path('register/',views.register,name='register'),
    path('userLogin/',views.userLogin,name='userLogin')
]
