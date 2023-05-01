
from django.contrib import admin
from django.urls import path
from home import views as home_views
from user_auth import views as auth_views
from event import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name="home"),
    path('login/', auth_views.login, name="login"),
    path('sign_up/', auth_views.sign_up, name="sign_up"),
    path('logout/', auth_views.logout, name="logout"),
    path('profile/', auth_views.profile, name="profile"), 
    path('events/', event_views.events, name="reserve"), 
]
