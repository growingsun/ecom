from django.contrib.auth.models import User
from Mineral.models import Customer
from django import forms


#CREATING FORMS FOR USER INPUT


class Customer_Reg(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:

        model = User
        fields = ('username','email','password')

class Customer_Info(forms.ModelForm):

    class Meta:

        model = Customer
        fields = ('website','product','product_image')








