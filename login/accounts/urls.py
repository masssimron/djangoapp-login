from django.urls import include, path
from . import views


urlpatterns = [
    
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('error',views.error,name='error'),
    path('logout',views.logout,name='logout')

]