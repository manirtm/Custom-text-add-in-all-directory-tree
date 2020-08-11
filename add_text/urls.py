from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logOutUser, name='logout'),
    path('customtext/', views.text_add, name='text_add'),
]