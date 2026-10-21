
from django.urls import path
from classschedulingApp.views import *

app_name="classschedulingApp"
urlpatterns = [
    path("", home_view, name="home"),
    path("login/", login_view, name="login"),
    path("logout/",logout_view,name="logout"),
    path("help/",help_View,name="help"),
    path("feedback/",feedback_View, name="feedback"),
    path("dashbord/",dashbord_view, name="dashbord"),
    
]
