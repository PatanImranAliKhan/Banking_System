from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage,name="home"),
    path('about/',views.AboutPage,name="about"),
    path('join/',views.AddDetails,name="join"),
    path('deposit/',views.TransferMoney,name="deposit"),
    path('deposit/<receiver>',views.TransferMoneySpecific,name="deposituser"),
    path('alltransactions/',views.TransactionsHistory,name="history"),
    path('cusdetails/',views.CustomerDetails,name="cusdetails"),
    path('addmoney/',views.AddMoneyPage,name="addmoney"),
    path('addmoney/<accnumber>',views.AddMoneyToAccount,name="addmoneyacc")
]