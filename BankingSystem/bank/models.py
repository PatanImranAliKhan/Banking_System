from django.db import models
from django import forms
from django.forms import TextInput,NumberInput,EmailInput

# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Accnumber=models.BigIntegerField(unique=True,blank=False, primary_key=True)
    balance=models.BigIntegerField()

class Transfer(models.Model):
    sender=models.BigIntegerField()
    reciever=models.BigIntegerField()
    amount=models.BigIntegerField()

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        widgets={
            'username': TextInput(attrs={'type':'text','placeholder':'User name','class':'form-control','name':'username'}),
            'email': EmailInput(attrs={'type':'email','placeholder':'example@gmail.com','class':'form-control','name':'email'}),
            'Accnumber': NumberInput(attrs={'type':'number','placeholder':'Account Number','class':'form-control','name':'Accnumber'}),
            'balance':NumberInput(attrs={'type':'number','placeholder':'Balance','class':'form-control','name':'balance'}),
        }

class TransferForm(forms.ModelForm):
    class Meta:
        model=Transfer
        fields='__all__'
        widgets={
            'sender': NumberInput(attrs={'type':'number','class':'form-control','name':'sender'}),
            'reciever':NumberInput(attrs={'type':'number','class':'form-control','name':'reciever'}),
            'amount':NumberInput(attrs={'type':'number','class':'form-control','name':'amount'}),
        }
