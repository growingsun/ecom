from django.conf.urls import url
from Mineral import views

app_name = 'Mineral'

urlpatterns = [


        url(r'^signup/$',views.min_signup,name="Sign Up"),
        url(r'^login/$',views.min_login,name="Login"),
        url(r'^$',views.min_home,name="Home"),
        url(r'^loginres/$',views.loginres,name="Login Response"),
        url(r'^logout/$',views.min_logout,name="Logout"),

]