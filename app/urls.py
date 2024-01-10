from django.urls import path
from . import views


urlpatterns = [
    path('', views.Dashboard, name="Dashboard"),
    path('logout', views.Logout, name="Logout"),
    path('deposite', views.Deposite, name="Deposite"),
    path('nav', views.Nav, name="Nav"),
    path('confirm', views.ConfirmInvest, name="ConfirmInvest"),
    path('withdraw', views.Withdraw, name="Withdraw"),
    path('invest', views.Invest, name="Invest"),
    path('history', views.History, name="History"),
    path('bannerad', views.BannerAd, name="BannerAd"),
    path('support', views.Support, name="Support"),
    path('referal', views.ReferalFxn, name="ReferalFxn"),
    path('profile', views.Profile, name="Profile"),
    path('confirmdeposite/<str:pk>/', views.ConfirmDeposite, name="ConfirmDeposite"),
    # path('maintenancedetails/<str:name>/', views.MaintainanceDetails, name="MaintainanceDetails"),
]


