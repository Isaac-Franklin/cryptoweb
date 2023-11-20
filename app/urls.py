from django.urls import path
from . import views


urlpatterns = [
    path('', views.Dashboard, name="Dashboard"),
    path('deposite', views.Deposite, name="Deposite"),
    path('nav', views.Nav, name="Nav"),
    path('confirm', views.ConfirmInvest, name="ConfirmInvest"),
    path('withdraw', views.Withdraw, name="Withdraw"),
    path('invest', views.Invest, name="Invest"),
    path('history', views.History, name="History"),
    path('support', views.Support, name="Support"),
    path('profile', views.Profile, name="Profile"),
    # path('maintenancedetails/<str:name>/', views.MaintainanceDetails, name="MaintainanceDetails"),
]


