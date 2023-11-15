from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('login/', views.login, name='login'),
    path("register/",views.register, name='register'),
    path("logout/", views.logout, name='logout'),
    path("confirm_email/",views.confirm_email, name='confirm_email'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path("account/", views.account, name='account'),
    path('notification/', views.notification, name='notification'),
    path("support", views.support, name='support'),
    path("support2", views.support2, name='support2'),
    path('dashboard',views.dashboard, name='dashboard'),
]