from django.shortcuts import render,redirect
from django.http import HttpResponse
from Userr .models import *
from Engineers .models import *
from django.db.models import Q


# Create your views here.
def index(request):
    if 'engineer_user' in request.session:
        return redirect('Engineer_home')
    else:
        return redirect('Engineer_login')


def engineersignupp(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        qulification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')
        category= request.POST.get('category')
        category = Category.objects.get(id=category)
        password = request.POST.get('password')
        print(category)
        if Engineer.objects.filter(Phone_number=mobile).exists():
            return render(request, 'Engineer_signup.html', {'mobile_exists': True})
        data = Engineer(Name=name, Phone_number=mobile, Email=email, Qualification=qulification, Experience=experience,Image=image, category=category, Password=password)
        data.save()
        return redirect('Engineer_index')
    else:
        categoryy = Category.objects.all().values()
        return render(request, 'signup.html', {'categoryy': categoryy,'mobile_exists': False})




def engineerlogin(request):

    if 'engineer_user' in request.session:
        return redirect('Engineer_home')
    else:

        if request.method == 'POST':
            print("POST")
            mobile = request.POST.get('mobile')
            # email= request.POST.get('email')
            password = request.POST.get('password')


            check_user = Engineer.objects.filter(Phone_number=mobile,Password=password)
            if check_user:
                request.session['engineer_user'] = mobile
                return redirect('Engineer_home')
            else:

                return render(request, 'Engineer_login.html', {'engineer_user': 'false'})
    return render(request, 'Engineer_login.html', {'engineer_user': 'null'})


def home(request):
    if 'engineer_user' in request.session:
        mobile = request.session['engineer_user']
        name = request.session['engineer_user']
        user = Engineer.objects.filter(Phone_number=mobile).first()
        enquiry = Engineer_contact_enquiryy.objects.filter(eng=mobile)

        return render(request, 'Engineer_home.html', {'engineer': user,'enquiry': enquiry})
    else:
        return redirect('Engineer_login')
# ========================================================================================================================================================




# ================================================================  Engineer View User remove block unblock ========================================
def eng_userview(request):
    if 'engineer_user' in request.session:
        euser = User.objects.all()
        if request.method == 'POST':
            search = request.POST.get('search')
            euser = User.objects.filter(Q(Name__icontains=search)| Q(Mobile__icontains=search)|Q(Email__icontains=search)|Q(Password__icontains=search)|Q(Status__icontains=search))
        return render(request,'Engineer_userview.html',{'eng_user':euser})

def eng_userblock(request,id):
    if 'engineer_user' in request.session:
        User.objects.filter(id=id).update(Status='Blocked')
        return redirect(eng_userview)


def eng_userunblk(request,id):
    if 'engineer_user' in request.session:
        User.objects.filter(id=id).update(Status='Active')
        return redirect(eng_userview)

def eng_userdelete(request,id):
    if 'engineer_user' in request.session:
        form = User.objects.get(id= id)
        form.delete()
        return redirect(eng_userview)

# ===========================================================================================================================================================



# ======================================================================== Engineer Project view remove =================================================================================
def addproject(request):
    if 'engineer_user' in request.session:
        engineer = request.session['engineer_user']
        eng = Engineer.objects.get(Phone_number=engineer)
        print(eng)
        if request.method == "POST":
            title = request.POST.get('title')
            description = request.POST.get('description')
            place = request.POST.get('place')
            start_date = request.POST.get('startdate')
            end_date = request.POST.get('enddate')
            contact = request.POST.get('contact')
            projectdata = Engineerproject(Project_Title=title,Project_description=description,Place=place,engineer=eng, Start_Date=start_date, End_Date=end_date,Contact_number=contact)
            projectdata.save()
        return render(request,'Engineer_projectadd.html')


def addprojectimage(request,id):
    if 'engineer_user' in request.session:
        img = Engineerproject.objects.get(id=id)
        print(img.id)
        if request.method == "POST":
            projectid = img.id
            image = request.FILES.get('image')
            print(projectid,image)
            imageadd = ProjectImage(ProjectImg=image,Project=img)
            print(imageadd)
            imageadd.save()
        return render(request,'Engineerproject_imgadd.html')



def engi_projectview(request):
    if 'engineer_user' in request.session:
        user = request.session['engineer_user']
        print(f'user email retrieved from session:{user}')
        engin= Engineer.objects.filter(Phone_number=user).first()
        print(engin.pk)
        if engin:
            project = Engineerproject.objects.filter(engineer=engin)
            print(project)

        return render(request,'Engineer_projectview.html',{'project':project})


def engineerprojectdelete(request,id):
    if 'engineer_user' in request.session:
        form = Engineerproject.objects.get(id= id)
        form.delete()
        return redirect(engi_projectview)





# ================================================================
def enuiryview(request):
    user = request.session['engineer_user']
    enginee = Engineer.objects.filter(Phone_number=user).first()
    if enginee:
        enquiry = Engineer_contact_enquiryy.objects.filter(eng=enginee)

    return render(request,'Engineer_enqiury.html',{'enquiry':enquiry})

def engineerenuirydelete(request,id):
    if 'engineer_user' in request.session:
        form = Engineer_contact_enquiryy.objects.get(id= id)
        form.delete()
        return redirect(enuiryview)




# =============================================================================================================================================


# ================================================================ Logout =================================================================================================
def engineerlogout(request):
    del request.session['engineer_user']

    return redirect(engineerlogin)


