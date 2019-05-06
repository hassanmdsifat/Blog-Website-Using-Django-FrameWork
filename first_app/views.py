from django.shortcuts import render
from first_app.models import Catagory,Post,Comment
from django.http import HttpResponseRedirect
from django import forms
# Create your views here.


def index(request):
     catagory_list=Catagory.objects.all().order_by("Name")
     get_data=Post.objects.all().order_by("-PostId")
     my_list={"catagory":catagory_list,"all_data":get_data}     
     return render(request,"first_app/index.html",my_list)

def about_me(request):
    catagory_list=Catagory.objects.all().order_by("Name")
    my_list={"catagory":catagory_list}
    return render(request,"first_app/aboutme.html",my_list)

def catagory(request):
    catagory_list=Catagory.objects.all().order_by("Name") 
    get_catagory=request.GET["cat"]
    new_cat=Catagory.objects.get(Name=get_catagory)
    ##print(new_cat.id)
    get_data=Post.objects.all().filter(Catagory=new_cat.id).order_by("-PostId")
    my_list={"catagory":catagory_list,"data":get_data,"current_catagory":get_catagory}
    return render(request,"first_app/catagory.html",my_list)


def details(request):
     catagory_list=Catagory.objects.all().order_by("Name")
     get_id=request.GET["id"]
     get_data=Post.objects.get(PostId=get_id)
     get_comments=Comment.objects.all().filter(PostId=get_id).order_by("-ComId")
     ##print(get_data.Title)
     my_list={"catagory":catagory_list,"Post_data":get_data,"all_comments":get_comments}
     return render(request,"first_app/seedetails.html",my_list)

def get_comments(request):
     catagory_list=Catagory.objects.all().order_by("Name")
     if request.method=="POST":
          email=request.POST["email"]
          comments=request.POST["message"]
          email=email.lstrip()
          comments=comments.lstrip()
          ##print("ASCHIIIII!!!!")
          if(email!="" and comments!=""):
               new_Comments=Comment()
               new_Comments.Message=comments
               new_Comments.Email=email
               new_Comments.PostId=request.GET["id"]
               new_Comments.save()
     next = request.POST.get('next', '/')
     next+="?id="
     next+=request.GET["id"]
     return HttpResponseRedirect(next)
     ##return details(request)
          