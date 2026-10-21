from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from classschedulingApp.models import *
from datetime import datetime, timedelta
from django.contrib.auth import authenticate


from django.utils import timezone
from datetime import datetime

from datetime import datetime

# Create your views here.
date_mounth_twenty_three = datetime.now() - timedelta(days=7)
date_mounth_twenty_four = datetime.now() - timedelta(days=6)
date_mounth_twenty_five = datetime.now() - timedelta(days=5)
date_mounth_twenty_six = datetime.now() - timedelta(days=4)
date_mounth_twenty_seven = datetime.now() - timedelta(days=3)
date_mounth_twenty_eight = datetime.now() - timedelta(days=2)
date_mounth_twenty_nine = datetime.now() - timedelta(days=1)
date_mounth_today = datetime.now() - timedelta(days=0)
 ##///---year one mounth one---////####
       
    
created_mounth_twenty_four = Notification.objects.filter(
date=date_mounth_twenty_four)
created_mounth_twenty_five = Notification.objects.filter(
date=date_mounth_twenty_five)
created_mounth_twenty_six = Notification.objects.filter(
date=date_mounth_twenty_six)
created_mounth_twenty_seven = Notification.objects.filter(
date=date_mounth_twenty_seven)
created_mounth_twenty_eight = Notification.objects.filter(
date=date_mounth_twenty_eight)
created_mounth_twenty_nine =Notification.objects.filter(
date=date_mounth_twenty_nine)
created_mounth_today = Notification.objects.filter(
date=date_mounth_today ,notify=1 )
def  dashbord_view(request):
    return redirect('admin:index')
def home_view(request, *args , **kwargs):
    if created_mounth_today.exists():
        update = f"Class Schedule was updated  "
        context= {"update":update}
        return render(request, "index.html",context)
         
    elif created_mounth_twenty_nine.exists():
        update = "Class Schedule was updated"
        context= {"update":update}
        return render(request, "index.html",context)
        
    elif created_mounth_twenty_eight.exists():
        update = "Class Schedule was updated"
        context= {"update":update}
        return render(request, "index.html",context)
       
    elif created_mounth_twenty_seven.exists():
        update = "Class Schedule was updated"
        context= {"update":update}
        return render(request, "index.html",context)
       
    elif created_mounth_twenty_six.exists():
        update = "Class Schedule was updated"
        context= {"update":update}
        return render(request, "index.html",context)
       
    elif created_mounth_twenty_five.exists():
        update = "Class Schedule was updated"
        context= {"update":update}
        return render(request, "index.html",context)
       
    elif created_mounth_twenty_four.exists():
        update = "Class Schedule was updated"
        context= {"update":update}
        return render(request, "index.html",context)
      
    else:
        return render(request, "index.html")
        


  
def login_view(request, *args , **kwargs):
    user  = request.user
    if user.is_authenticated:
        return redirect("classschedulingApp:home")
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        #loginuser = authenticate(request,usename=username,password=password)
        loginuser = authenticate(request,username=username,password=password)
        if loginuser:
            login(request, loginuser)
            messagessuccess=' welcome back!'
            context= {'messagessuccess':messagessuccess}
            
            
            return redirect("classschedulingApp:home")
        messagessuccess='Username and Password Incorrect'
        context= {'messagessuccess':messagessuccess}
        return render(request,"login.html",context)
            
    
    return render(request,"login.html")


def logout_view(request, *args , **kwargs):
    request.session.clear()


    return redirect("classschedulingApp:home")

def help_View(request):

    return render(request,"help.html")

def feedback_View(request):
    user = request.user
    if request.method =="GET":
        feedback = FeedBack.objects.all()
        context = {"feedback":feedback}
        return render(request,"feedback.html", context)
    if request.method =="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if user.student==True:

            feedbacksave = FeedBack.objects.create(

                name=name,
                student=True,
                instructor=False,
                senderid= user.id ,
                email=email,
                subject=subject,
                message=message,
                            )
            feedbacksave.save()

            feedbackmessage = "Thank you for your Feedback!"
            context = {"feedbackmessage":feedbackmessage}

            return render(request,"feedback.html", context)
        elif user.instructor==True:
            feedbacksave = FeedBack.objects.create(

                name=name,
                    student=False,
                instructor=True, 
                   
                email=email,
                subject=subject,
                message=message,
                            )
            feedbacksave.save()
            feedbackmessage = "Thank you for your Feedback!"
            context = {"feedbackmessage":feedbackmessage}

            return render(request,"feedback.html", context)
        else:
            context = {"feedback":feedback}
            return render(request,"feedback.html", context)










    


    
