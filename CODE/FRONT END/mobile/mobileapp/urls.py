from django.urls import path

from .views import MobileApp
from .views import ReLog
from .views import UserHome

urlpatterns = [
    path('',MobileApp.index,name='index'),
    path('about/',MobileApp.about,name='about'),
    path('login/',ReLog.login,name='login'),
    path('register/',ReLog.register,name='register'),
    path('checkmail/',ReLog.checkmail,name='checkmail'),
    path('changepass/',ReLog.changepass,name='changepass'),
    path('uhome/',UserHome.uhome,name='uhome'),
    path('view/',UserHome.view,name='view'),
    path('train/',UserHome.train,name='train'),
    path('pred/',UserHome.pred,name='pred'),
]
