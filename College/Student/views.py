from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



#   This Function will extract all the users from form and saved in database if it's a POST request or if it's get just dispaly a create view
def Studnet_From(request):
    if request.method=="POST":

        #Student Persnol infomration
        Roll_Form = request.POST['rolno']
        Fname_Form = request.POST['Name']
        Class_Form = request.POST['Class']
        Mobile_Form = request.POST['Mobile']
        Adress_form = request.POST['Address']

        #   Stduent Academics informations
        Maths_Score   = request.POST['mahts']
        Physics_Score = request.POST['physics']
        Chemistry_Score= request.POST['chemistry']
        Biology_Score  = request.POST['biology']
        English_Score = request.POST.get('english')

        #Collect the data save to database
        Studentper_info = models.StudentInfo(RoleNo=Roll_Form,  Name=Fname_Form, Class=Class_Form, Mobile=Mobile_Form, Address=Adress_form)
        Stduentacd_info = models.StudentAcademics(RoleNo_id=Roll_Form, Maths=Maths_Score, Physics=Physics_Score, Chemistry=Chemistry_Score, Biology= Biology_Score, English=English_Score)
        Studentper_info.save()
        Stduentacd_info.save()
        return render(request, "index.html")

    else:
        return render(request, "Student_Form.html")


# login_required is decoratore is used to dispaly only if users is logged in

@login_required(login_url="account/Login")
def Display_info(request):
    info1 = models.StudentInfo.objects.all()

    return render(request, "Display_info.html", {"Student_info":info1})

# Here it will display Accademic scores for all
@login_required(login_url="account/Login")
def Display_accdemic(request, pk):
    info = models.StudentAcademics.objects.get( RoleNo = pk )
    info1 = models.StudentInfo.objects.get( RoleNo = pk )
    return render(request, "display_Accinfo.html", {"std_score":info, "role_num":pk, "std_info":info1 })

def index(request):
    return render(request, "index.html")


def Search(request):
    if request.method  == "POST":
        Searched_value = request.POST.get('search')
        info1 = models.StudentInfo.objects.filter(Name=Searched_value).exists()
        if info1 == True:
            value = models.StudentInfo.objects.get(Name=Searched_value)
            print(value.Name)
            return render(request, "Search.html", {"S_Value": value})
        else:
            messages.info(request, ("User_does't exsits"))
            return render(request, "Search.html")


    else:
        return render(request, "Search.html")


def Signup(request):
    return render(request, "signup.html")



def Confirm_delet(request, pk):
    info = models.StudentInfo.objects.get( RoleNo = pk )
    models.StudentInfo.objects.get( RoleNo = pk ).delete()
    return render(request, "Confirm_delet.html", {"Delted_user": info}
    )


def Update_user(request, pk):
    info = models.StudentInfo.objects.get( RoleNo = pk )
    return render(request, "Update_userlist.html", {"Update_user": info} )


def Display_Searched_user(request):
    Name = request.POST.get('search')
    try:
        info = models.StudentInfo.objects.get(Name = Name )
        print(info.Class)
        return render(request, "Sucessful.html")
    except:
        print("An exception occurred")
        return render(request, "Sucessful.html")

def Update_From_userlst(request):
    Roll_Form = request.POST.get('rolno')
    Fname_Form = request.POST.get('name')
    Class_Form = request.POST.get('class')
    Mobile_Form = request.POST.get('mobile')
    Adress_form = request.POST.get('address')
    value_to_update  = models.StudentInfo.objects.get( RoleNo = Roll_Form)
    value_to_update.Name = Fname_Form
    value_to_update.Class = Class_Form
    value_to_update.Mobile = Mobile_Form
    value_to_update.Address = Adress_form
    value_to_update.save()
    return redirect("/Display_info")

def Update_And_Delete(request):
    info1 = models.StudentInfo.objects.all()
    info2 = models.StudentAcademics.objects.all()
    return render(request, "Update_And_Delete.html" , {"Student_info1": info1})
