from django.shortcuts import render,redirect
from Engineers .models import *
from Adminn.models import *
from django.contrib.auth import authenticate,login,logout
from Adminn .form import *
from django.db.models import Q

# Create your views here.
def axiom_admin(request):
    if request.user.is_authenticated:
        count_user = User.objects.count()
        count_enineer = Engineer.objects.count()
        count_projects = Engineerproject.objects.count()
    return render(request,'index.html',{'count':count_user, 'count_enineer':count_enineer,'projects':count_projects})


def admin_login(request):
    if request.user.is_authenticated:
        return redirect(axiom_admin)
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(password,username)

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(axiom_admin)
            else:
                return render(request,'admin_login.html')


        return render(request,'admin_login.html')


# ========================================== Category ADD REMOVE VIEW ===============================
def addcategory(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AdminCategoryModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(addcategory)
        else:
            form = AdminCategoryModelForm()
    else:
        return redirect('adminlogin')

    return render(request, 'add_category.html',{'form':form})

def admincategory_view(request):
    if request.user.is_authenticated:
        form = Category.objects.all()
        return render(request,'admincategory_view.html', {'formm':form})

def categorydelete(request,id):
    if request.user.is_authenticated:
        form = Category.objects.get(id= id)
        form.delete()
        return redirect(admincategory_view)
# =============================================== Category ADD REMOVE VIEW closeeeeeeeeee =============================



# =======================================================================================================================

def enquiry_view(request):
    if request.user.is_authenticated:
        form = Admin_UserEnquiry.objects.all()
        return render(request,'adminenquiry_view.html', {'formm':form})
def enquiry_delete(request,id):
    if request.user.is_authenticated:
        form = Admin_UserEnquiry.get(id= id)
        form.delete()
        return redirect(enquiry_view)


# =========================================== User View DELETE BLOCK UNBLOCK ==============================================

def userview(request):
    if request.user.is_authenticated:
        form = User.objects.all()
        if request.method == 'POST':
            search = request.POST.get('search')
            form = User.objects.filter(Q(Name__icontains=search)| Q(Mobile__icontains=search)|Q(Email__icontains=search)|Q(Password__icontains=search)|Q(Status__icontains=search))
        return render(request,'adminuser_view.html',{'data':form})

def userblock(request,id):
    if request.user.is_authenticated:
        User.objects.filter(id=id).update(Status='Blocked')
        return redirect(userview)


def userunblk(request,id):
    if request.user.is_authenticated:
        User.objects.filter(id=id).update(Status='Active')
        return redirect(userview)

def userdelete(request,id):
    if request.user.is_authenticated:
        form = User.objects.get(id= id)
        form.delete()
        return redirect(userview)


# ============================================= User View DELETE BLOCK UNBLOCK closeeeeeeeeee ============================
# =====================================================================================================================



# =========================================== Engineer View DELETE BLOCK UNBLOCK =============================================================

def engineerview(request):
    if request.user.is_authenticated:
        form = Engineer.objects.all()
        if request.method == 'POST':
            search = request.POST.get('search')
            form = Engineer.objects.filter(Q(Name__icontains=search)| Q(Email__icontains=search)|Q(Phone_number__icontains=search)|Q(Qualification__icontains=search)|Q(Experience__icontains=search)|Q(category__Name__icontains=search)|Q(Password__icontains=search)|Q(Create_at__icontains=search)|Q(Status__icontains=search))
        return render(request,'adminengineer_view.html',{'data':form})

def engineerrequest(request):
    if request.user.is_authenticated:
        form = Engineer.objects.filter(Status='Pending')
        return render(request,'admin_requested_engineer.html',{'data':form})
def engineerapprove(request,id):
    if request.user.is_authenticated:
        Engineer.objects.filter(id=id).update(Status='Active')
        return redirect(engineerview)



def engineerblock(request,id):
    if request.user.is_authenticated:
        Engineer.objects.filter(id=id).update(Status='Blocked')
        return redirect(engineerview)


def engineerunblk(request,id):
    if request.user.is_authenticated:
        Engineer.objects.filter(id=id).update(Status='Active')
        return redirect(engineerview)

def engineerdelete(request,id):
    if request.user.is_authenticated:
        form = Engineer.objects.get(id= id)
        form.delete()
        return redirect(engineerview)




# =============================================== Engineer View DELETE BLOCK UNBLOCK closeeeeeeee ==========================================




# ============================================================


def adminprojectview(request):
    if request.user.is_authenticated:
        form = Engineerproject.objects.all()
        if request.method == 'POST':
            search = request.POST.get('search')
            form = Engineerproject.objects.filter(Q(Project_Title__icontains=search)| Q(Project_description__icontains=search)|Q(engineer__Name__icontains=search)|Q(Place__icontains=search)|Q(Start_Date__icontains=search)|Q(End_Date__icontains=search)|Q(Contact_number__icontains=search))
        return render(request,'admin_project view.html',{'data':form})

def adminprojectdelete(request,id):
    if request.user.is_authenticated:
        form = Engineerproject.objects.get(id= id)
        form.delete()
        return redirect(adminprojectview)



def adminreview_view(request):
    if request.user.is_authenticated:
        form = Review.objects.all()
        return render(request,'adminreview_view.html',{'data':form})
def adminreviewdelete(request,id):
    if request.user.is_authenticated:
        form = Review.objects.get(id= id)
        form.delete()
        return redirect(adminreview_view)

# ========================================================= LOGOUT =====================================================================
def admin_logout(request):

    if request.user.is_authenticated:
        logout(request)
        return redirect('adminlogin')
    else:
        return render(request, 'admin_login.html')

# ============================================================ LOGOUT CLOSE ==============================================================


