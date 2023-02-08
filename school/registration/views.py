from django.shortcuts import render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import redirect



# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalide credential')
            return redirect(request,'login')

    return render(request,'login.html')

def reg(request):
    if request.method=='POST':
        username=request.POST['name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name taken')
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')

                return redirect('reg')
            else:
               user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password,last_name=last_name)

               user.save();
               return redirect('login')


        else:
         messages.info(request,'invalid password')
        return redirect('reg')
    # return redirect('index')

    return render(request,'reg.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
