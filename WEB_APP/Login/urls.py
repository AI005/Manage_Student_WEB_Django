from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ClassLogin.as_view(), name = "login"),
    #path('', auth_views.LoginView.as_view(template_name="Login/login.html"), name="login"),
    #('logout/',auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]