from django.urls import path
from . import views 
from . views import TaskCreate


urlpatterns = [
    path('',views.home,name="home"),
    
    path('login/',views.loginpage,name="login"),

    path('register/',views.register,name="register"),

    path('taskcreate/',TaskCreate.as_view(),name="taskscreate"),

    path('myself/',views.myself,name="myself"),

    path('profile/',views.view_profile,name='profile'),

    path('account/', views.accountSettings, name="account"),
    
    path('socialmedia/',views.social,name="socialmedia"),   

    path('userslist/',views.diplayusername,name='userlist'),
    
    path('logout/',views.logoutUser,name="logout"),
     
    
    
    #path('user/',views.userpage,name='user'),
    #path('taskcreate/',views.TaskCreate,name="taskscreate"),
]
