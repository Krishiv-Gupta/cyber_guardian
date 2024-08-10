from django.urls import path
from . import views


urlpatterns=[
    path("",views.home,name='home'),
    path('play',views.play,name='play'),
    path('test',views.test,name='test'),
    path('safe',views.safe,name='safe'),
    path('send',views.send,name='send'),
    path('signup',views.signup,name='signup'),
    path('sign1',views.sign1, name='sign1')
]