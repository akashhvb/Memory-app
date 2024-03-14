from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User


# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        fn=request.POST['first_name']
        last_name=request.POST['last-name']
        
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=fn,
            last_name=last_name

        )
        user.save()
        auth.login(request,user)
        print("user created")
        return redirect('/')
    return render(request,"reg.html")
def logout(request):
      auth.logout(request)
      return redirect('/accounts/login')

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"credental does not match")
            return redirect('/accounts/login')
    return render(request,"login.html")




