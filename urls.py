from django.conf.urls import url
from register import views

# SET THE NAMESPACE!
app_name = 'register'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    #url(r'^register/$',views.register,name='register'),
    #url(r'^adduser/$',views.adduser,name='adduser'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^emp_signup/$',views.emp_signup,name='emp_signup'),
    url(r'^emplogin/$',views.emplogin,name='emplogin'),
    url(r'^welcome/$',views.welcome,name='welcome'),
]
