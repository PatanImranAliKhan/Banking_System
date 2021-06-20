from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer, Transfer, CustomerForm, TransferForm
import re

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def AboutPage(request):
    return render(request, 'about.html')

def CustomerDetails(request):
    try:
        customers=Customer.objects.all()
        if request.method=="POST":
            results = []
            name = str(request.POST['search'])
            c=0
            for i in customers:
                if re.match(name, i.username, re.IGNORECASE):
                    results.append(i)
                    c=c+1
            if(isinstance(accno, int)):
                for i in customers:
                    if name in str(i.Accnumber):
                        results.append(i)
                        c=c+1
            if c!=0:
                return render(request, 'details.html',{'customers':results})
            return render(request,'details.html',{'error': "no results found"})
        return render(request, 'details.html',{'customers':customers})
    except:
        return render(request, 'details.html')

def AddMoneyPage(request):
    if(request.method=="POST"):
        accnumber=int(request.POST['accnumber'])
        amount=int(request.POST['amount'])
        data=Customer.objects.get(Accnumber=accnumber)
        data.balance=data.balance+amount
        data.save()
        return  render(request, 'addMoney.html',{'message':"money has been added"})
    return  render(request, 'addMoney.html')

def AddMoneyToAccount(request,accnumber):
    if(request.method=="POST"):
        amount=int(request.POST['amount'])
        data=Customer.objects.get(Accnumber=int(accnumber))
        data.balance=data.balance+amount
        data.save()
        return  render(request, 'addMoney.html',{'message':"money has been added"})
    return  render(request, 'addMoney.html',{'accnumber':accnumber})

def TransactionsHistory(request):
    try:
        transfers=Transfer.objects.all()
        if request.method=="POST":
            results = []
            name = str(request.POST['search'])
            c=0
            for i in transfers:
                if name in str(i.sender):
                    l=[i.sender,i.reciever,i.amount]
                    results.append(l)
                    print(l)
                    c=c+1
            for i in transfers:
                if name in str(i.reciever):
                    l=[i.sender,i.reciever,i.amount]
                    results.append(l)
                    c=c+1
            i=0
            while(i<len(results)):
                a=results[i]
                p=results.count(a)
                if(p>1):
                    while(results.count(a)!=1):
                        results.remove(a)
                i=i+1
            print(results)
            if c!=0:
                return render(request, 'alltransactions.html',{'transfers':results})
            return render(request,'alltransactions.html',{'error': "no results found"})
        data=[]
        c=0
        for i in transfers:
            l=[i.sender,i.reciever,i.amount]
            data.append(l)
            c+=1
        if(c==0):
            return render(request, 'alltransactions.html',{'error':"No transactions has not done."})
        return render(request, 'alltransactions.html',{'transfers':data})
    except:
        return render(request, 'alltransactions.html',{'error':"No transactions has not done."})

def TransferMoney(request):
    try:
        tform=TransferForm()
        if(request.method=="POST"):
            transferform=TransferForm(request.POST)
            sen=request.POST['sender']
            rec=request.POST['reciever']
            money=request.POST['amount']
            if(sen==rec):
                error="Sender details and Receiver details are same"
                return render(request, 'Deposit.html',{'form':tform,'error':error})
            try:
                data1=Customer.objects.get(Accnumber=sen)
                try:
                    data2=Customer.objects.get(Accnumber=rec)
                    d=data1.balance
                    print(d,"   ",money)
                    if(d<=int(money)):
                        error="Not have sufficient money to deposit"
                        return render(request, 'Deposit.html',{'form':tform,'error':error})
                    print(transferform.is_valid())
                    if(transferform.is_valid()):
                        data1.balance=d-int(money)
                        data1.save()
                        data2.balance=data2.balance+int(money)
                        data2.save()
                        transferform.save()
                        message="Transaction has been succeed"
                        return render(request, 'Deposit.html',{'form':tform,'message':message})
                    error="Error in transaction"
                    return render(request, 'Deposit.html',{'form':tform,'error':error})
                except:
                    error="The Receiver data was incorrect"
                    return render(request, 'Deposit.html',{'form':tform,'error':error})
            except:
                error="The Sender data was incorrect"
                return render(request, 'Deposit.html',{'form':tform,'error':error})
        return render(request, 'Deposit.html',{'form':tform})
    except:
        error="Given Data was incorrect"
        return render(request, 'Deposit.html',{'form':tform,'error':error})

def AddDetails(request):
    aform=CustomerForm()
    if(request.method=="POST"):
        form=CustomerForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            message="Data has been Saved successfully"
            return render(request, 'join.html',{'form':aform,'message':message})
        else:
            error="Something error has been occured"
            return render(request, 'join.html',{'form':aform,'error':error})
    return render(request, 'join.html',{'form':aform})

def TransferMoneySpecific(request,receiver):
    try:
        tform=TransferForm()
        if(request.method=="POST"):
            tranform=TransferForm(request.POST)
            sen=request.POST['sender']
            rec=receiver
            money=request.POST['amount']
            if(sen==rec):
                error="Sender details and Receiver details are same"
                return render(request, 'Deposit.html',{'form':tform,'error':error})
            try:
                data1=Customer.objects.get(Accnumber=sen)
                try:
                    data2=Customer.objects.get(Accnumber=rec)
                    d=data1.balance
                    if(d<=int(money)):
                        error="Not have sufficient money to deposit"
                        return render(request, 'Deposit.html',{'form':tform,'error':error,'receiver':receiver})
                    print(d,"   ",money)
                    t=Transfer(sender=int(sen),reciever=int(receiver),amount=int(money))
                    print("hello")
                    data1.balance=d-int(money)
                    data1.save()
                    data2.balance=data2.balance+int(money)
                    data2.save()
                    t.save()
                    message="Transaction has been succeed"
                    return render(request, 'Deposit.html',{'form':tform,'message':message})
                except:
                    error="The Receiver data was incorrect"
                    return render(request, 'Deposit.html',{'form':tform,'error':error,'receiver':receiver})
            except:
                error="The Sender data was incorrect"
                return render(request, 'Deposit.html',{'form':tform,'error':error,'receiver':receiver})
        return render(request, 'Deposit.html',{'form':tform,'receiver':receiver})
    except:
        error="Given Data was incorrect"
        return render(request, 'Deposit.html',{'form':tform,'error':error})