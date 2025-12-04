from app .views import *

from django.urls import path
urlpatterns = [
    path("",home, name="home"),
    path("contact/",contact, name="contact"),
    path('wealth-management', wealthmanagemen, name='wealthmanagemen'),
    path('about', about, name='about'),
    path('business-banking', business, name='business'),
    path('contact', contact, name='contact'),
    path('financialiq', financialiq, name='financialiq'),
    path('setmap', setmap, name='setmap'),
    path('location', location, name='location'),
    path('search', location, name='location'),
    path('service', service, name='service'),
    path('caeeres', caeeres, name='caeeres'),
    path('corporate', corporate, name='corporate'),
    path('security', security, name='security'),
    path('checkingsavig', checkingsavig, name='checkingsavig'),
    path('personalloan', personalloan, name='personalloan'),
    path('Investmentinsta', Investmentinsta, name='Investmentinsta'),
    path('homeloan', homeloan, name='homeloan'),
    path('vehiclelloan', vehiclel, name='vehiclel'),
    path('bankproduct', bankproduct, name='bankproduct'),
    path('creditcard', creditcard, name='creditcard'),
    path('policy', policy, name='policy'),
    path('privacy', policy, name='policy'),
    path('alumi', alumi, name='alumi'),
    path('accessablitiy', accessablitiy, name='accessablitiy'),

    # auth
    path("accounts/login/",Loginuser, name="Loginuser"),
    path("verify/<pk>/",verify, name="verify"),
    path("block/",block, name="block"),
    path("register/",registeruser, name="registeruser"),
    path("logout/",logoutuser, name="logoutuser"),
    # end auth
    path("policy/",policy, name="policy"),
 
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