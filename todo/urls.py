from django.urls import path
from . import views



urlpatterns = [

    path('', views.home, name= ''), 
    
    path('register', views.Register, name="register"),

    path('login', views.LoginPage, name="login"),

    path('dashboard', views.Dashboard, name="dashboard"),

    path('profile-management', views.Profile_Management, name="profile-management"),
    
    path('delete-account', views.DeleteAccount, name="delete-account"),
    
    path('create', views.Create, name="create"),

    path('read', views.Read, name="read"),

    path('update/<str:pk>/', views.Update, name="update"),

    path('delete/<str:pk>/', views.Delete, name="delete"),
    
    path('logout', views.Logout, name="logout"),
]