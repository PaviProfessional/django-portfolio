from django.shortcuts import render
from django.contrib import messages
from base import models
from base.models import Contact 

# Create your views here
def home(request):
    return render(request,'home.html')

def letstalk(request):
    return render(request,'contact.html')

def youtube(request):
    return render(request,'youtube.html')

def ecommerce(request):
    return render(request,'ecommerce.html')

def portfolio(request):
    return render(request,'myportfolio.html')



def contact(request):
   if request.method=="POST":
       print('post')
       name=request.POST.get('name')
       email=request.POST.get('email')
       number=request.POST.get('number')
       content=request.POST.get('content')
       print(name,email,number,content )

       if len(name)>1 and len(name)<30:
           pass
       else:
           messages.error(request,'Lenght of name should be greater than 2 and less than 30 words ')
           return render(request,'home.html')
       
       if len (email)>1 and len(email)<30:
           pass
       else:
           messages.error(request,'invaild email try again ')
           return render(request,'home.html')
       print(len(number))
       if  len(number)>9 and len(number)<13:
           pass
       else:
           messages.error(request,'invaild number please try again ')
           return render(request,'home.html')
       ins = models.Contact(name=name,email=email,content=content,number=number)
       ins.save()
       messages.success(request,'Thank You for contacting me!! Your message has been saved ')
       print('data has been saved to database')
 
       print('The request is no pass ')
   return render(request,'home.html') 


  
