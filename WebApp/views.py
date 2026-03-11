from django.shortcuts import render,redirect
from WebApp.models import *
from AdminApp.models import AddcategoryDb
# Create your views here.

def sign_in(request):
    return render(request,"sign_in.html")

def sign_up(request):
    return render(request, "sign_up.html")


def home_page(request):
    category = AddcategoryDb.objects.all()
    return render(request,"home.html",{"category":category})

def save_user(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pswrd = request.POST.get('password')
        con_pass = request.POST.get('confirm_password')
        obj = UserDb(Username=uname,Email=email,Password=pswrd,Confirm_password=con_pass)
        obj.save()
        return redirect(sign_in)

def user_login(request):
        if request.method == "POST":
            uname = request.POST.get("username")
            pswrd = request.POST.get("password")
        if UserDb.objects.filter(Username=uname, Password=pswrd).exists():
            request.session['Username'] = uname
            request.session['Password'] = pswrd
            return redirect(home_page)
        else:
            return redirect(sign_up)
    
def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(home_page)



def report_issue(request):
    category = AddcategoryDb.objects.all()
    return render(request,"report_issue.html",{"category":category})

def all_post(request):
    user = UserDb.objects.all()
    category = AddcategoryDb.objects.all()
    issues = IssueDb.objects.all()
    return render(request,"all_post.html",{"issues":issues,"user":user,"category":category})

def save_contact(request):
    if request.method == "POST":
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        desc = request.POST.get('desc')
        obj = ContactDb(Full_Name=name,Email=email,Mobile=mobile,Description=desc)
        obj.save()
    
    return redirect(home_page)

def save_issue(request):
    if request.method == "POST":
        cat = request.POST.get('category_name')
        issue_img = request.FILES.get('img')
        desc = request.POST.get('desc')
        con_number = request.POST.get('contact_number')
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        location = request.POST.get('location')
        uname = request.POST.get('uname')

        obj = IssueDb(Category=cat,Image=issue_img,Description=desc,Contact_Number=con_number,
                      Latitude=lat,Longitude=lon,Location=location,Username=uname)
        obj.save()
    return redirect(home_page)


def save_comments(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        com = request.POST.get('comment')
        issue_id = request.POST.get('issue_id')
        obj=CommentDb(Comment=com,Username=uname,Issue_id=issue_id)
        obj.save()
    return redirect(all_post)

def view_details(request,issue_id):
    category = AddcategoryDb.objects.all()
    details = IssueDb.objects.filter(id=issue_id)
    comments = CommentDb.objects.filter(Issue_id=issue_id).order_by("-id")
    return render(request,"view_details.html",{"details":details,"comments":comments,"category":category})
