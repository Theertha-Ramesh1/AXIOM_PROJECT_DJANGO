from django.shortcuts import render,redirect
from django.http import HttpResponse
from Engineers .models import *
from Userr .models import *
from Adminn.models import *
from django.db.models import Q



# Create your views here.

# <!--category selecting time corresponding engineers show -->

# from django.http import JsonResponse
#
# def get_engineers(request):
#     category_id = request.GET.get('category_id')
#     engineers = Engineer.objects.filter(category=category_id).values('id', 'Name')
#     return JsonResponse(list(engineers), safe=False)


def index(request):
    if 'user' in request.session:
        return redirect('home')
    else:
        return redirect('login')


def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(Mobile=mobile).exists():
            return render(request, 'signup.html', {'mobile_exists': True})
        data = User(Name=name, Mobile=mobile, Email=email, Password=password)
        data.save()
        return redirect('index')
    else:
        return render(request, 'signup.html', {'mobile_exists': False})


def login(request):
    print("login")
    if 'user' in request.session:
        return redirect('home')
    else:
        if request.method == 'POST':
            print("POST")
            mobile = request.POST.get('mobile')
            # email= request.POST.get('email')
            password = request.POST.get('password')
            check_user = User.objects.filter(Mobile=mobile,Password=password)
            if check_user:
                request.session['user'] = mobile
                return redirect('home')
            else:
                print("KKK")
                return render(request, 'login.html', {'user': 'false'})
    return render(request, 'login.html', {'user': 'null'})







def profileedit(request):
    if 'user' in request.session:
        userdata = User.objects.get(Mobile=request.session['user'])
        data = User.objects.filter(Mobile=request.session['user'])
        print(data.values())
        if request.method == 'POST':
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            password = request.POST.get('password')
            userdata.Name = name
            userdata.Mobile = mobile
            userdata.Email = email
            userdata.Password = password
            userdata.save()
        return render(request, 'editprofile.html', {'data': data})

def home(request):
    if 'user' in request.session:
        recently_visited = request.session.get('recently_visited', [])
        print(recently_visited)
        recent_project = Engineerproject.objects.filter(id__in=recently_visited)[2:]
        mobile = request.session['user']
        user = User.objects.filter(Mobile=mobile)
        engineer = Engineer.objects.all()[:4]
        proje = Engineerproject.objects.all()[:4]
        imag = ProjectImage.objects.filter()[:4]
        # recently_visited = request.session.get('user', [])
        project = request.session.get('project',0)
        project= int(project)
        project= project+1
        request.session['project'] = project


        return render(request, 'home.html', {'user': user, 'engineer': engineer, 'proje': proje, 'imag': imag, 'recently_visited': recent_project})
    else:
        return redirect('login')

def engineers(request):
    if 'user' in request.session:
        engineer = Engineer.objects.all()
        return render(request,'engineers.html',{'engineerdata':engineer})


def project(request):
    if 'user' in request.session:
        proect = Engineerproject.objects.all()
        if request.method == 'POST':
            # project_id = Engineerproject.objects.get(id=id)
            # print(project_id)
            search = request.POST.get('search')
            proect = Engineerproject.objects.filter(Q(Project_Title__icontains=search) | Q(Project_description__icontains=search) | Q(Place__icontains=search) | Q(Contact_number__icontains=search))
        # else:
        #     recently_visited = request.session.get('user',[])
        #     recently_visited.insert(0,id)
        #     request.session['user'] = recently_visited

        return render(request, 'project.html', {'projet': proect})

def wishlist(request):
    if 'user' in request.session:
        user = request.session['user']
        print(user)
        # project_id = Engineerproject.objects.filter(id=id)
        wishlist = Wishlist.objects.filter(user=User.objects.get(Mobile=user))
        print(wishlist.values())
    return render(request,'wishlist.html',{'wishlist':wishlist})


def individualproject(request,id):
    if 'user' in request.session:
        engineer_prjt_obj = Engineerproject.objects.get(id=id)
        recently_visited = request.session.get('recently_visited',[])
        recently_visited.insert(0,id)
        request.session['recently_visited'] = recently_visited
        projimg = ProjectImage.objects.filter(Project=id)
        projecttt = Engineerproject.objects.filter(id=id)
        review = Review.objects.filter(Project=engineer_prjt_obj)
        if request.method == 'POST':
            project_id = Engineerproject.objects.get(id=id)
            user_id = User.objects.get(id=id)
            data = Wishlist(project=project_id,user=user_id)
            data.save()

        # user = ImageUser.objects.filter(user_id=)
        return render(request, 'individualproject.html', {'projecttt': projecttt, 'projimg': projimg, 'review': review})

def individualprofile(request,id):
    if 'user' in request.session:
        eng = Engineer.objects.get(id=id)
        engineer = Engineer.objects.filter(id=id)
        projet = Engineerproject.objects.filter(engineer=Engineer.objects.get(id=id))
        context = {'aboutengineer': engineer, 'projet': projet}
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            location = request.POST.get('location')
            purpose = request.POST.get('purpose')
            data = Engineer_contact_enquiryy(name=name, address=address, email=email, phone_number=phone, location=location, purpose=purpose,eng=eng)
            data.save()
        return render(request,'individualprofile.html',context)



def contactengineer(request):
    return render(request,'contactengineer.html')

def enquiry(request):
    if 'user' in request.session:
        # catego = Category.objects.all()
        # userrr = User.objects.all()
        # categorry = request.GET.get('category')
        # engi = Engineer.objects.filter(category=categorry).values('Name')
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            location = request.POST.get('location')
            purpose = request.POST.get('purpose')
            data = Admin_UserEnquiry(Name=name,Address=address,Email=email,Phone=phone,Location=location,Purpose=purpose)
            data.save()
        return render(request,'enquiry.html')






def plans(request):
    return render(request,'plans.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('index')
    return redirect('login')



