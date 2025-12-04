from django.shortcuts import render
from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User  # To associate with Django's built-in User model
from django.db.models import Q
from .genUid import *
from .req import *
# Create your views here.
 
def home(request):
    return render(request, "home/main.html")
def wealthmanagemen(request):
    return render(request, "home/wealth-managemen.html")
def Investmentinsta(request):
    return render(request, "home/Investmentinsta.html")
def about(request):
    return render(request, "home/about.html")
def business(request):
    return render(request, "home/business.html")
def contact(request):
    return render(request, "home/contact.html")
def financialiq(request):
    return render(request, "home/financialiq.html")
def location(request):
    return render(request, "home/location.html")
def corporate(request):
    return render(request, "home/corporate.html")
def caeeres(request):
    return render(request, "home/caeeres.html")
def security(request):
    return render(request, "home/security.html")
def checkingsavig(request):
    return render(request, "home/checkingsavig.html")
def creditcard(request):
    return render(request, "home/creditcard.html")
def personalloan(request):
    return render(request, "home/personalloan.html")
def homeloan(request):
    return render(request, "home/homeloan.html")
def vehiclel(request):
    return render(request, "home/vehicleload.html")
def service(request):
    return render(request, "home/service.html")
def bankproduct(request):
    return render(request, "home/bankproduct.html")
def accessablitiy(request):
    return render(request, "home/accessablitiy.html")
def alumi(request):
    return render(request, "home/alumi.html")
def policy(request):
    return render(request, "home/policy.html")
def setmap(request):
    return render(request, "home/setmap.html")


from django.core.mail import send_mail,  EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from  django.utils.html import strip_tags
from django.conf import settings

# emal

def email_sending(request,tempname,context,subjects,to):
    try:
        tos = render_to_string(tempname,context=context )
        tags =strip_tags(tos)
        mas = EmailMultiAlternatives(
            subject = subjects,
            body=tags,
            from_email = settings.EMAIL_HOST_USER,
            to=[to]
            )
        mas.attach_alternative(tos, 'text/html')
        mas.send()
    except:
        pass

# AUth?


def passwordchange(request,pk):
    try:
        if Account.objects.filter(uuid=pk).exists():
            dd = Account.objects.get(uuid=pk)
            if request.method =="POST":
                curren = request.POST['currentp']
                password = request.POST['password']
                new = request.POST['new']
                if dd.password == curren:
                    if password == new:
                        dd.password = new
                        dd.save()
                        messages.info(request, 'successfully change password')
                        return redirect('passwordchange', pk=dd.uuid)
                    else:
                        messages.info(request, 'password mismatch')
                else:
                    messages.info(request, 'current password incorrect')
                        
                    
        
            
            
    except:
        pass
    con ={
        'user':dd ,
        'site':siteedit.objects.get(idx=1)
        
    }
    return render(request, 'user/passwordchange.html',con)

def verify(request,pk):
    try:
        if Account.objects.filter(uuid=pk).exists():
            dd = Account.objects.get(uuid=pk)
            dd.appoved =True
            dd.save()
            print(dd)
        else:
            dd= None
            
            
    except:
        pass
    con ={
        'user':dd ,
        'site':siteedit.objects.get(idx=1)
        
    }
    return render(request, 'auth/approve.html',con)

def block(request):
    if Account.objects.filter(user=request.user).exists():
        ee = Account.objects.get(user=request.user)
        con ={
                'site':siteedit.objects.get(idx=1),
                'user':ee,
            }
        email_sending(request,'mail/block.html',con,"Account Blocked ",ee.user.email.lower())
    else:
        ee= 'USER'       
    con ={
        # 'user':ee,
        'site':siteedit.objects.get(idx=1)
        
    }    
    return render(request, 'auth/block.html',con)
def Loginuser(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if Account.objects.filter(username=username, password=password).exists():
            user = Account.objects.get(username=username, password=password)
            con ={
                    'site':siteedit.objects.get(idx=1),
                    'user':user,
                    'link':f'{request.get_host()}/verify/{user.uuid}/'

                }
            if Account.objects.filter(username=username, password=password, disable=True).exists(): 
                email_sending(request,'mail/block.html',con,"Account Blocked ",user.user.email.lower())
                messages.info(request, 'Account has been Blocked.')
                return redirect("Loginuser")
            elif user.appoved == False :
                email_sending(request,'mail/acct.html',con,"Account Verification ",user.user.email.lower().replace(" ", ""))
                messages.info(request, 'Please check your email for verification.')
                return redirect("Loginuser")
            elif user.user.is_superuser:
                authenticate(request, username=username, password=password)

                login(request, user.user)

                return redirect("adminuserxx", pk=user.uuid)
            else:
                authenticate(request, username=username, password=password)

                login(request, user.user)

                return redirect("dashboard", pk=user.uuid)
                
        else:
                messages.error(request, 'user does not exist')        
        
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "auth/Login.html",con)
def registeruser(request):
    print(f'{request.get_host()}/verify/')
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        occupation = request.POST['occupation']
        email = request.POST['email']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        phone = request.POST['phone']
        dob = request.POST['dob']
        gender = request.POST['gender']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        status = request.POST['status']
        account_type = request.POST['account_type']
        prefered_cur = request.POST['prefered_cur']
        picName = request.POST['picName']
        if User.objects.filter(Q(username= username) | Q(email=email)  ).exists() and len(firstname) <= 25:
            messages.error(request, 'username and email already taken')
            return redirect('registeruser') 
        else:
            if password == password2:
                
                setuse = User.objects.create(username = username, email=email, first_name =firstname, last_name = lastname)
                setmain = Account.objects.create(user = setuse, password =password, 
                                                 
                account_type=account_type,
                uuid=genUdis(22),
                accountnum = acc(),
                    preferred_currency=prefered_cur,
                    status = status,
                    photo=picName,
                    gender=gender,
                    username=username,
                    date_of_birth=dob,
                    phone=phone,
                    zipcode=zipcode, 
                    address = address, 
                    state=state,
                    country=country,
                    occupation=occupation,
                    city=city,
                    swiftcode=generate_swift_code(),
                                                 )
                setmain.save()
                setuse.save()
                
                con ={
                     'site':siteedit.objects.get(idx=1),
                     'user':setuse,
                     'link':f'{request.get_host()}/verify/{setmain.uuid}/'
                    }
                email_sending(request,'mail/acct.html',con,"Account Verification ",email.lower().replace(" ", ""))
                messages.info(request, 'Please check your email for verification.')
                return redirect('Loginuser') 
                
            else:
                messages.error(request, 'password doest match')
                   
    con ={
        'site':siteedit.objects.get(idx=1)
    }
    return render (request, "auth/register.html",con)
def logoutuser(request):
    logout(request)
    
    return redirect('Loginuser')



@account_enabled_required
def dashboard(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/dashboard.html",con)
# dashboar?
@account_enabled_required
def profile(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/profile.html",con)

@account_enabled_required
def addaccount(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/addaccount.html",con)

 
@account_enabled_required
def depositehis(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/hsitoryd.html",con)

@account_enabled_required
def benefit(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
        if request.method == 'POST':
            swift = request.POST['swift']
            account_number = request.POST['account_number']
            bank_name = request.POST['bank_name']
            email = request.POST['email']
            phone = request.POST['phone']
            account_name = request.POST['account_name']
            if swift and email:
                benfitx.objects.create(
                    uuid=referCode(7),
                    accname = account_name,
                    accnum = account_number ,
                    bankname = bank_name,
                    email = email,
                    phone = phone,
                    swiftcode = swift,
                    appoved = 'pending',
                )
                messages.info(request, "Success! The beneficiary has been added successfully.")
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/benefit.html",con)


@account_enabled_required
def benefithis(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/benfithis.html",con)

@account_enabled_required
def deposit(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
        if request.method =="POST":
                amount = request.POST['amount']
                method = request.POST['method']
                if amount and method:
                    cc = depositex.objects.create(
                        uuid=referCode(6),
                        Amount=amount,
                        method=method
                        
                    )
                    user.deposite.add(cc)
                    messages.info(request, 'Deposit is Onprocess')
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/deposite.html",con)
@account_enabled_required
def hsitory(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/hsitory.html",con)

@account_enabled_required
def intertansfer(request, pk):
    if True:
        user = Account.objects.get(uuid = pk)
         
        if request.method =="POST":
                bank_name = request.POST['bank_name']
                acct_no = request.POST['acct_no']
                r_name = request.POST['r_name']
                iban_number = request.POST['iban_number']
                swift_code = request.POST['swift_code']
                country = request.POST['country']
                address = request.POST['address']
                amount = request.POST['amount']
                desc = request.POST['desc']
                if user.balance >= int(amount)  :
                    xx = intertransferx.objects.create(
                        uuid=referCode(7),
                        accname = r_name,
                        accnum = acct_no,
                        bankname=bank_name,
                        swiftcode = swift_code,
                        ibannumber = iban_number,
                        ountry = country,
                        Description =desc,
                        Amount =int(amount),
                        appoved ='pending'  
                    )
                    user.intertransfer.add(xx)
                    user.balance -=int(amount)
                    con ={
                        'site':siteedit.objects.get(idx=1),
                        "user":user,
                        'item':xx
                    }
                    email_sending(request,'mail/interdebite.html',con,f"Debit Alert[{user.preferred_currency}{amount}]",user.user.email.lower())
                    
                    user.save()
                    messages.info(request, 'The transfer is being processed')
                else:
                    messages.info(request, 'Insufficient Fund')
                    
        
    # except:
    #     return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/intertranfer.html",con)


@account_enabled_required
def loan(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
        
        if request.method =="POST":
                type = request.POST['loan_type']
                amount = request.POST['loan_amount']
                netincom = request.POST['income']
                dis = request.POST['loan_desc']
                if type and amount:
                    dd =  loanx.objects.create(
                        uuid=referCode(8),
                        Amount=amount,
                        Types=type,
                        NetIncome=netincom,
                        Description=dis,
                        appoved='pending'
                    )
                    user.loan.add(dd)
                    messages.info(request, 'Loan is on review ')
                    return redirect('loanhis', pk=user.uuid)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/loan.html",con)


@account_enabled_required
def loanhis(request, pk):
    try:
        user = Account.objects.get(uuid = pk)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/loanhis.html",con)

@account_enabled_required
def loacltranfer(request, pk):
    if True:
        user = Account.objects.get(uuid = pk)
        if request.method =="POST":
                accname = request.POST['accname']
                accnum = request.POST['accnum']
                bankname = request.POST['bankname']
                amount = request.POST['amount']
                dis = request.POST['dis']
                if user.balance >= int(amount):
                    locattrand = localtransferx.objects.create(uuid=referCode(8),accname=accname,bankname=bankname,
                                                               accnum=accnum,Amount=amount,Description=dis ,appoved='pending')
                    user.localtransfer.add(locattrand)
                    user.balance -= int(amount)
                    user.save()
                    con ={
                        'site':siteedit.objects.get(idx=1),
                        "user":user,
                        'item':locattrand
                    }
                    email_sending(request,'mail/interdebite.html',con,f"Debit Alert[{user.preferred_currency}{amount}]",user.user.email.lower())
                    return redirect('hsitory', user.uuid)
                else:
                    messages.info(request, 'Insufficient fund')
                    return redirect('loacltranfer', user.uuid)
                    
    # except:
    #     return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "user":user
    }
    return render (request, "user/localtransfer.html",con)







# Admin


from .form import *

from django.shortcuts import render, redirect, get_object_or_404



@superuser_required
def adminuserxx(request, pk):
    if True:
        alluser = Account.objects.get(user=request.user)
        alluserx = Account.objects.all().exclude(user=alluser.user)

    # except:
    #     return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "alluserx":alluserx
    }
    return render (request, "adminx/home.html",con)


@superuser_required
def admincreateuser(request, pk):
    if True:
        alluser = Account.objects.get(user=request.user)

 
        itemget = Account.objects.all()
        if request.method == 'POST':
            firstname = request.POST['first-name']
            lastname = request.POST['last-name']
            occupation = request.POST['occupation']
            email = request.POST['email']
            address = request.POST['address']
            country = request.POST['country']
            city = request.POST['city']
            state = request.POST['state']
            zipcode = request.POST['zipcode']
            phone = request.POST['phone']
            dob = request.POST['dob']
            gender = request.POST['gender']
            username = request.POST['username']
            password = request.POST['password']
            status = request.POST['status']
            account_type = request.POST['account_type']
            prefered_cur = request.POST['prefered_cur']
            picName = request.POST['picName']
            if User.objects.filter(Q(username= username) | Q(email=email)  ).exists():
                messages.error(request, 'username and email already taken')
                return redirect('admincreateuser',pk=pk) 
                
            else:
                if password:
                    
                    setuse = User.objects.create(username = username, email=email, first_name =firstname, last_name = lastname)
                    setmain = Account.objects.create(user = setuse, password =password, 
                                                    
                    account_type=account_type,
                    uuid=genUdis(22),
                    accountnum = acc(),
                        preferred_currency=prefered_cur,
                        status = status,
                        photo=picName,
                        gender=gender,
                        username=username,
                        date_of_birth=dob,
                        phone=phone,
                        zipcode=zipcode, 
                        address = address, 
                        state=state,
                        country=country,
                        occupation=occupation,
                        city=city,
                        swiftcode=generate_swift_code(),
                                                    )
                    setmain.save()
                    setuse.save()
                
               
                    messages.info(request, 'create succesfully')
                    return redirect('admincreateuser',pk=pk) 
                    
                else:
                    messages.error(request, 'password doest match')
     
    # except:
    #     return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "itemget":itemget,
    }
    return render (request, "adminx/createuser.html",con)


@superuser_required
def adminupdateuser(request, pk):
    if True:
        alluser = Account.objects.get(user=request.user)
        account = get_object_or_404(Account, uuid=pk)
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=account)
            if form.is_valid():
                form.save()
                return redirect('adminupdateuser', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = ProfileForm(instance=account)
    # except:
    #     return redirect('Loginuser')  
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "form":form
    }
    return render (request, "adminx/updateuser.html",con)


@superuser_required
def localtransfer(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)

        item = localtransferx.objects.all()
       
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
    }
    return render (request, "adminx/localtranser.html",con)

@superuser_required
def intertransfer(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)

        item = intertransferx.objects.all()
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
    }
    return render (request, "adminx/interlog.html",con)

@superuser_required
def createintertransfer(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        
        item = intertransferx.objects.all()
        if request.method == 'POST':
            form = InterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, 'created successfully')
                return redirect('createintertransfer', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = InterForm()
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)

@superuser_required
def updateintertransfer(request, pk):
    if True:
        alluser = Account.objects.get(user=request.user)
        
        item = intertransferx.objects.all()
        account = intertransferx.objects.get(uuid=pk)
        print(account)
        if request.method == 'POST':
            form = InterForm(request.POST, instance=account)
            if form.is_valid():
                print(form.cleaned_data['appoved'])
                form.save()
                messages.info(request, "Updated successfully")
                return redirect('updateintertransfer', pk=pk)  # Redirect to a profile detail view after saving
            else:
                print(form.errors)
        else:
            form = InterForm(instance=account)
    # except:
    #     return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)

@superuser_required
def createlocalransfer(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)

        item = localtransferx.objects.all()
        if request.method == 'POST':
            form = localForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, 'created successfully')
                return redirect('createlocalransfer', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = localForm()
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)

@superuser_required
def updatelocaltransfer(request, pk):
    if True:
        alluser = Account.objects.get(user=request.user)

        item = localtransferx.objects.all()
        account = localtransferx.objects.get( uuid=pk)
        print(account)
        if request.method == 'POST':
            form = localForm(request.POST, instance=account)
            if form.is_valid():
                form.save()
                messages.info(request, "Updated successfully")
                return redirect('updatelocaltransfer', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = localForm(instance=account)
    # except:
    #     return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)




def createloan(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        
        item = loanx.objects.all()
        if request.method == 'POST':
            form = loanForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, 'created successfully')
                return redirect('createloan', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = loanForm()
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)


def updateloan(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        item = loanx.objects.all()
        account = get_object_or_404(loanx, uuid=pk)
        if request.method == 'POST':
            form = loanForm(request.POST, instance=account)
            if form.is_valid():
                form.save()
                messages.info(request, "Updated successfully")
                return redirect('updateloan', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = loanForm(instance=account)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)





@superuser_required
def adminload(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)

        allloan = loanx.objects.all()
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":allloan,
    }
    return render (request, "adminx/loanlog.html",con)

@superuser_required
def createbene(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        
        item = benfitx.objects.all()
        if request.method == 'POST':
            form = benefitForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, 'created successfully')
                return redirect('createloan', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = benefitForm()
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)
def updatebene(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        
        item = benfitx.objects.all()
        account = get_object_or_404(benfitx, uuid=pk)
        if request.method == 'POST':
            form = benefitForm(request.POST, instance=account)
            if form.is_valid():
                form.save()
                return redirect('updatebene', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = benefitForm(instance=account)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)





def admibene(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        
        allloan = benfitx.objects.all()
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":allloan,
    }
    return render (request, "adminx/benelog.html",con)


def createdeposit(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        
        item = depositex.objects.all()
        if request.method == 'POST':
            form = depositForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, 'created successfully')
                return redirect('createdeposit', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = depositForm()
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)
def updatedeposit(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        
        item = depositex.objects.all()
        account = get_object_or_404(depositex, uuid=pk)
        if request.method == 'POST':
            form = depositForm(request.POST, instance=account)
            if form.is_valid():
                form.save()
                return redirect('updatedeposit', pk=pk)  # Redirect to a profile detail view after saving
        else:
            form = depositForm(instance=account)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":item,
        "form":form,
    }
    return render (request, "adminx/createintertransfer.html",con)





def admideposit(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        
        allloan = benfitx.objects.all()
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "item":allloan,
    }
    return render (request, "adminx/depsite.html",con)









def localitem(request, pk):
    if True:
        itemx = Account.objects.get(user=request.user)
        mainotem = localtransferx.objects.get(uuid = pk)
    # except:
    #     return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":itemx,
        "item":mainotem
    }
    return render (request, "adminx/detailpage.html",con)
def interitem(request, pk):
    if True:

        itemx = Account.objects.get(user=request.user)
        mainotem = intertransferx.objects.get(uuid = pk)

    # except:
    #     return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":itemx,
        "item":mainotem,
        
    }
    return render (request, "adminx/detailpage.html",con)

def admindeleteuser(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)

    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser
    }
    return render (request, "adminx/delete.html",con)


def fund(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        userx =  Account.objects.all().exclude(id=alluser.id)
        if request.method == "POST":
            user =  request.POST['user']
            typex =  request.POST['type']
            amount =  request.POST['amount']
            date =  request.POST['date']
            dis =  request.POST['dis']
            if Account.objects.filter(uuid = user).exists():
                useracc = Account.objects.get(uuid = user)
                if int(amount):
                    c = localtransferx.objects.create(
                            accname = get_random_name(),
                            accnum = acc() ,
                            uuid = genUdis(6),
                            bankname =get_random_bank_name(),
                            Amount = amount,
                            Description = dis,
                            appoved='completed',
                            date=date,
                            )
                    c.save()
                    useracc.localtransfer.add(c)
                    if typex == "debit":
                        useracc.balance -= int(amount)
                        useracc.save()
                        messages.info(request, 'successfully')
                        return redirect('fund', pk=alluser.uuid)
                    if typex == "credit":
                        useracc.balance += int(amount)
                        useracc.save()
                        messages.info(request, 'successfully')
                        return redirect('fund', pk=alluser.uuid)
                else:
                        
                        messages.info(request, 'insufficient fund')
                        return redirect('fund', pk=alluser.uuid)
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
        "userx":userx,
    }
    return render (request, "adminx/fund.html",con)
def siteadmin(request, pk):
    try:
        alluser = Account.objects.get(user=request.user)
        item = siteedit.objects.get(idx = 1)
        if request.method  == "POST":
            logo = request.POST['picName']
            name = request.POST['name']
            email = request.POST['email']
            domain = request.POST['domain']
            address = request.POST['address']
            country = request.POST['country']
            dis = request.POST['dis']
            phone = request.POST['phone']
            if siteedit.objects.filter(idx = 1).exists():
                item.logo = logo or item.logo
                item.name = name
                item.country = country
                item.email = email
                item.Address =  address
                item.dis = dis
                item.phone = phone
                item.domain = domain
                item.save()
                messages.info(request, 'Updated successfully')
                return redirect('siteadmin', pk=alluser.uuid)   
                
            else:
                siteedit.objects.create(
                    logo=logo, name=name, email=email, country=country, 
                    dis=dis, phone=phone, domain=domain,Address=address
                    
                )
                messages.info(request, 'created successfully')
                return redirect('siteadmin', pk=alluser.uuid)   
    except:
        return redirect('Loginuser')
    con ={
        'site':siteedit.objects.get(idx=1),
        "alluser":alluser,
    }
    return render (request, "adminx/site.html",con)














# deleteing,



def localdelete(request, pk):
    if True:
        mainuser = Account.objects.get(user=request.user)
        
        item = localtransferx.objects.get(uuid=pk)
        item.delete()
        messages.info(request, 'deleted successfully')
        return redirect('localtransfer', pk=mainuser.uuid)
    
    # except:
    #     return redirect('Loginuser')
def interdelete(request, pk):
    try:
        mainuser = Account.objects.get(user=request.user)
        item = intertransferx.objects.get(uuid=pk)
        item.delete()
        messages.info(request, 'deleted successfully')
        return redirect('intertransfer', pk=mainuser.uuid)
    except:
        return redirect('Loginuser')
def Loandelete(request, pk):
    try:
        mainuser = Account.objects.get(user=request.user)
        item = loanx.objects.get(uuid=pk)
        item.delete()
        messages.info(request, 'deleted successfully')
        
        return redirect('adminload', pk=mainuser.uuid)
    except:
        return redirect('Loginuser')
def benedelete(request, pk):
    try:
        mainuser = Account.objects.get(user=request.user)
        item = benfitx.objects.get(uuid=pk)
        item.delete()
        messages.info(request, 'deleted successfully')
        
        return redirect('admibene', pk=mainuser.uuid)
    except:
        return redirect('Loginuser')
def userdelete(request, pk):
    try:
        mainuser = Account.objects.get(user=request.user)
        
        item = Account.objects.get(uuid=pk)
        s =User.objects.get(id=item.user.id)
        s.delete()
        item.delete()
        messages.info(request, 'deleted successfully')
        
        return redirect('adminuserxx', pk=mainuser.uuid)
    except:
        return redirect('Loginuser')
  