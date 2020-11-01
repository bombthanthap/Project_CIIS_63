from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ciis_app.models import *


def participant_home(request):
    return render(request,"participant_templates/participant_home.html")

def participant_payment_history(request):
    return render(request,"participant_templates/participant_payment_history.html")

def participant_payment(request):
    return render(request,"participant_templates/participant_payment.html")

def participant_upload_payment(request):
    return render(request,"participant_templates/participant_upload_payment.html")

def participant_edit_infomation(request):
    return render(request,"participant_templates/participant_edit_infomation.html")


def participant_payment_2(request):
    #num=memberparticipant.objects.values_list('id',flat=True)
    #idmax=max(num)
    #print(idmax)
    #data = memberparticipant.object.fliter(idmax=request.idmax,user=request.user) 
    
    
    
    data = memberparticipant.object.values_list('id',flat=True)
    
    idmax=max(data)
    
    data2 = memberparticipant.object.filter(id=idmax)
    


    dataall = memberparticipant.object.filter(user=request.user,id=idmax)
    return render(request,"participant_templates/participant_payment_2.html",{"dataall":dataall})
    



def new(request):
    return render(request,"participant_templates/new.html")

def new_save(request):
    
    if request.method!="POST":
       return HttpResponse("Method Not Allowed")
       
    else:
        num=request.POST.get("num")
        numall= num*1000
        banquet=request.POST.get("banquet")
        radio=request.POST.get("inline1")
        firstname=request.POST.get("inputFirstName1")
        lastname=request.POST.get("inputLastName1")
        email=request.POST.get("inputemail1")

        person = "1"
        peperlist = "CIIS 2021"
        status = "Inprogess"
        allmoney="10000"

        if radio == "1 person : 2000 Bath":
            radio=request.POST.get("inline1")
        else:
            radio="0"

        try:
            regis=participantmember(radio=radio,num=num,numall=numall,person=person,banquet=banquet,paperlist=peperlist,status=status,allmoney=allmoney,firstname1=firstname,lastname1=lastname,email1=email)
            regis.save()
            return HttpResponseRedirect(reverse("participant_home"))
        except:
            return HttpResponseRedirect(reverse("new"))




def participant_payment_save(request):
    if request.method!="POST":
       return HttpResponse("Method Not Allowed")
       
    else:
        
        banquet=request.POST.get("banquet")

        


        radio1=request.POST.get("inline")
        
        #print(radio1)
        
        
       


            
        try:
            paperlist = "CIIS 2020"
            
            
            
            
            if radio1 == "1":
                 
                person=request.POST.get("inline")
                price1= int(2000)
                
                price2= int(banquet)*int(1000)
                price = price1+price2
                
                
                

                firstname1=request.POST.get("inputFirstName1")
                lastname1=request.POST.get("inputLastName1")
                email1=request.POST.get("inputemail1")
            
               


                regis=memberparticipant(person=person,price=price,user=request.user,paperlist=paperlist,banquet=banquet,firstname1=firstname1,lastname1=lastname1,email1=email1)
                #firstname2=firstname2,lastname2=lastname2,email2=email2,firstname3=firstname3,lastname3=lastname3,email3=email3,firstname4=firstname4,lastname4=lastname4,email4=email4,firstname5=firstname5,lastname5=lastname5,email5=email5)
                if (firstname1 == "") or (lastname1 == "") or (email1 == ""):
                    raise ValueError()
                regis.save()
                

                



            if radio1 == "2":

                person=request.POST.get("inline")
                price1= int(4000)
                price2= int(banquet)*int(1000)
                price = price1+price2
                firstname1=request.POST.get("inputFirstName1")
                lastname1=request.POST.get("inputLastName1")
                email1=request.POST.get("inputemail1")
                firstname2=request.POST.get("inputFirstName2")
                lastname2=request.POST.get("inputLastName2")
                email2=request.POST.get("inputemail2")
                    
                regis=memberparticipant(person=person,price=price,user=request.user,paperlist=paperlist,banquet=banquet,firstname1=firstname1,lastname1=lastname1,email1=email1,firstname2=firstname2,lastname2=lastname2,email2=email2)
                if (firstname1 == "") or (lastname1 == "") or (email1 == "") or (firstname2 == "") or (lastname2 == "") or (email2 == ""):
                    raise ValueError()
                
                regis.save()

                

            if radio1 == "3":
                
                person=request.POST.get("inline")
                price1= int(6000)
                price2= int(banquet)*int(1000)
                price = price1+price2
                firstname1=request.POST.get("inputFirstName1")
                lastname1=request.POST.get("inputLastName1")
                email1=request.POST.get("inputemail1")
                firstname2=request.POST.get("inputFirstName2")
                lastname2=request.POST.get("inputLastName2")
                email2=request.POST.get("inputemail2")
                firstname3=request.POST.get("inputFirstName3")
                lastname3=request.POST.get("inputLastName3")
                email3=request.POST.get("inputemail3")
                regis=memberparticipant(person=person,price=price,user=request.user,paperlist=paperlist,banquet=banquet,firstname1=firstname1,lastname1=lastname1,email1=email1,firstname2=firstname2,lastname2=lastname2,email2=email2,firstname3=firstname3,lastname3=lastname3,email3=email3)
                if (firstname1 == "") or (lastname1 == "") or (email1 == "") or (firstname2 == "") or (lastname2 == "") or (email2 == "")  or (firstname3 == "") or (lastname3 == "") or (email3 == ""):
                    raise ValueError()
                regis.save()
           
            if radio1 == "4":
                person=request.POST.get("inline")
                price1= int(8000)
                price2= int(banquet)*int(1000)
                price = price1+price2
                firstname1=request.POST.get("inputFirstName1")
                lastname1=request.POST.get("inputLastName1")
                email1=request.POST.get("inputemail1")
                firstname2=request.POST.get("inputFirstName2")
                lastname2=request.POST.get("inputLastName2")
                email2=request.POST.get("inputemail2")
                firstname3=request.POST.get("inputFirstName3")
                lastname3=request.POST.get("inputLastName3")
                email3=request.POST.get("inputemail3")
                firstname4=request.POST.get("inputFirstName4")
                lastname4=request.POST.get("inputLastName4")
                email4=request.POST.get("inputemail4")
                regis=memberparticipant(person=person,price=price,user=request.user,paperlist=paperlist,banquet=banquet,firstname1=firstname1,lastname1=lastname1,email1=email1,firstname2=firstname2,lastname2=lastname2,email2=email2,firstname3=firstname3,lastname3=lastname3,email3=email3,firstname4=firstname4,lastname4=lastname4,email4=email4)
                if (firstname1 == "") or (lastname1 == "") or (email1 == "") or (firstname2 == "") or (lastname2 == "") or (email2 == "")  or (firstname3 == "") or (lastname3 == "") or (email3 == "") or (firstname4 == "") or (lastname4 == "") or (email4 == ""):
                    raise ValueError()
                
                regis.save()

            if radio1 == "5":
                person=request.POST.get("inline")
                price1= int(10000)
                price2= int(banquet)*int(1000)
                price = price1+price2
                firstname1=request.POST.get("inputFirstName1")
                lastname1=request.POST.get("inputLastName1")
                email1=request.POST.get("inputemail1")
                firstname2=request.POST.get("inputFirstName2")
                lastname2=request.POST.get("inputLastName2")
                email2=request.POST.get("inputemail2")
                firstname3=request.POST.get("inputFirstName3")
                lastname3=request.POST.get("inputLastName3")
                email3=request.POST.get("inputemail3")
                firstname4=request.POST.get("inputFirstName4")
                lastname4=request.POST.get("inputLastName4")
                email4=request.POST.get("inputemail4")
            
                firstname5=request.POST.get("inputFirstName5")
                lastname5=request.POST.get("inputLastName5")
                email5=request.POST.get("inputemail5")
                regis=memberparticipant(person=person,price=price,user=request.user,paperlist=paperlist,banquet=banquet,firstname1=firstname1,lastname1=lastname1,email1=email1,firstname2=firstname2,lastname2=lastname2,email2=email2,firstname3=firstname3,lastname3=lastname3,email3=email3,firstname4=firstname4,lastname4=lastname4,email4=email4,firstname5=firstname5,lastname5=lastname5,email5=email5)
                if (firstname1 == "") or (lastname1 == "") or (email1 == "") or (firstname2 == "") or (lastname2 == "") or (email2 == "")  or (firstname3 == "") or (lastname3 == "") or (email3 == "") or (firstname4 == "") or (lastname4 == "") or (email4 == "") or (firstname5 == "") or (lastname5 == "") or (email5 == ""):
                    raise ValueError()
                
                regis.save()

            


            return HttpResponseRedirect(reverse("participant_payment_2"))

        except ValueError:
            messages.error(request,"Fill Incorrect")
            return HttpResponseRedirect(reverse("participant_payment"))
        except Exception as e:
            print(e)
            return HttpResponseRedirect(reverse("participant_payment_history"))