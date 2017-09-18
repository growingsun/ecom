from django.shortcuts import render
from Mineral.forms import Customer_Reg,Customer_Info
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse



# Create your views here.



myname = "none"


def min_home(request):

    return render(request,"mineral/mineral_home.html")


def min_signup(request):

    registered = False
    if request.method == "POST":

        customer_reg_form = Customer_Reg(data=request.POST)
        customer_info_form = Customer_Info(data=request.POST)

        if customer_reg_form.is_valid() and customer_info_form.is_valid():

            newregform = customer_reg_form.save()
            newregform.set_password(newregform.password)
            newregform.save()

            newinfoform = customer_info_form.save(commit=False)
            newinfoform.name = newregform

            if 'product_image' in request.FILES:
                newinfoform.product_image = request.FILES['product_image']

            newinfoform.save()
            registered = True

        else:

            return render(request,"mineral/signupfailed.html")

    else:

        customer_reg_form = Customer_Reg()
        customer_info_form = Customer_Info()

    return render(request,"mineral/signup.html",
                  {'cusform':customer_reg_form,
                   'cusinfoform':customer_info_form,
                   'signed':registered})

@login_required
def min_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("Mineral:Login"))



def min_login(request):

    if request.method == "POST":

        c_name = request.POST.get('uname')
        global myname
        myname = c_name
        c_password = request.POST.get('password')
        user = authenticate(request,username=c_name,password=c_password)

        if user:
            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse("Mineral:Login Response"))

            else:

                return HttpResponse("Your account is not active")

        else:

            return render(request,"mineral/loginfailed.html")
    else:

        return render(request,"mineral/login.html")


def loginres(request):

    profile_info = {'user_name':myname}
    return render(request,"mineral/loginresponse.html",context=profile_info)



