from app.views import *

from django.urls import path
urlpatterns = [
    path("",home, name="home"),
    path("contact/",contact, name="contact"),
    path("savingacc/",savingacc, name="savingacc"),
    path("checkingacc/",checkingacc, name="checkingacc"),
    path("bchecking/",bchecking, name="bchecking"),
    path("baccount/",baccount, name="baccount"),
    path("blending/",blending, name="blending"),
    path("bcreditcard/",bcreditcard, name="bcreditcard"),
    path("investment/",investment, name="investment"),
    # auth
    path("accounts/login/",Loginuser, name="Loginuser"),
    path("verify/<pk>/",verify, name="verify"),
    path("block/",block, name="block"),
    path("register/",registeruser, name="registeruser"),
    path("logout/",logoutuser, name="logoutuser"),
    # end auth
    path("policy/",policy, name="policy"),
    path("lending/",lending, name="lending"),
    path("carrer/",carrer, name="carrer"),
    path("creditcard/",creditcard, name="creditcard"),
     
    
    
    
    
    # dashb
    path("localdetail/<pk>/",localitem, name="localitem"),
    path("interdetail/<pk>/",interitem, name="interitem"),
    
    
    
    path("dashboard/<pk>/",dashboard, name="dashboard"),
    path("passwordchange/<pk>/",passwordchange, name="passwordchange"),
    path("profile/<pk>/",profile, name="profile"),
    path("addaccount/<pk>/",addaccount, name="addaccount"),
    path("benefit/<pk>/",benefit, name="benefit"),
    path("dhistory/<pk>/",depositehis, name="depositehis"),
    path("benefithis/<pk>/",benefithis, name="benefithis"),
    path("deposit/<pk>/",deposit, name="deposit"),
    path("history/<pk>/",hsitory, name="hsitory"),
    path("intertansfer/<pk>/",intertansfer, name="intertansfer"),
    path("loan/<pk>/",loan, name="loan"),
    path("loanhis/<pk>/",loanhis, name="loanhis"),
    path("loacltranfer/<pk>/",loacltranfer, name="loacltranfer"),
    
    
    
    # Admin
    path("adminuserxx/<pk>/",adminuserxx, name="adminuserxx"),
    path("fund/<pk>/",fund, name="fund"),
    path("userdelete/<pk>/",userdelete, name="userdelete"),
    path("siteadmin/<pk>/",siteadmin, name="siteadmin"),
    path("admincreateuser/<pk>/",admincreateuser, name="admincreateuser"),
    path("admiinlocaltransfer/<pk>/",localtransfer, name="localtransfer"),
    path("admiinintertransfer/<pk>/",intertransfer, name="intertransfer"),
    path("createlocalransfer/<pk>/",createlocalransfer, name="createlocalransfer"),
    path("createintertransfer/<pk>/",createintertransfer, name="createintertransfer"),
    path("updatelocaltransfer/<pk>/",updatelocaltransfer, name="updatelocaltransfer"),
    path("updateintertransfer/<pk>/",updateintertransfer, name="updateintertransfer"),
    path("adminload/<pk>/",adminload, name="adminload"),
    path("createloan/<pk>/",createloan, name="createloan"),
    path("updateloan/<pk>/",updateloan, name="updateloan"),
    path("admibene/<pk>/",admibene, name="admibene"),
    path("benedelete/<pk>/",benedelete, name="benedelete"),
    path("createbene/<pk>/",createbene, name="createbene"),
    path("interdelete/<pk>/",interdelete, name="interdelete"),
    path("Loandelete/<pk>/",Loandelete, name="Loandelete"),
    path("localdelete/<pk>/",localdelete, name="localdelete"),
    path("updatebene/<pk>/",updatebene, name="updatebene"),
    path("adminupdateuser/<pk>/",adminupdateuser, name="adminupdateuser"),
    path("admindeleteuser/<pk>/",admindeleteuser, name="admindeleteuser"),
    
    
]