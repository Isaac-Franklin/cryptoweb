from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserSignUpFxn, name="UserSignUpFxn"),
    # path('login', views.UserLogin, name="UserLogin"),
    path('logout', views.UserLogout, name="UserLogout"),
    path('referal/<str:username>', views.ReferedUser, name="ReferedUser"),
    # path('maintenancedetails/<str:name>/', views.MaintainanceDetails, name="MaintainanceDetails"),
]


