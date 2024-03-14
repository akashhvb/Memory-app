
from email.mime import image
from django.shortcuts import render,redirect
from memoryapp.models import Post,Profile

# Create your views here.
def index(request):
     all_memo = Post.objects.all()
     return render(request,"index.html",{"all_memo":all_memo})
def profile(request):
    if request.mrthod=="POST"and request.FILES.items():
        image=request.FILES["image"]
        contact=request.POST["contact"]

        profile, created=Profile.objects.get_or_create(
            user_image=image,
            contact=contact,
            user=request.user,
        )

def post(request):
    if request.method=="POST":
        image=request.POST["image"]
        caption=request.POST["caption"]
    
        post, created =Post.objects.get_or_create(
           user=request.user,
           image= image,
           caption = caption,
        )
        return redirect("/")
    else:
        return render(request,"post.html")

