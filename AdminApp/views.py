from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from AdminApp.models import *
from WebApp.models import *


# Create your views here.


def dashboard(request):
    return render(request,"dashboard.html")
# *********************************************************************************
def admin_login_page(request):
    return render(request,"AdminLoginPage.html")

def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pswrd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            data=authenticate(username=uname, password=pswrd)
            if data is not None:
                login(request, data)
                request.session['username'] = uname
                request.session['password'] = pswrd
                return redirect(dashboard)
            else:

                return redirect(admin_login_page)
        else:

            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

# *********************************************************************************

def add_category(request):
    return render(request,"categories.html")

def save_category(request):
    if request.method == "POST":
        cat_name = request.POST.get("category_name")
        obj = AddcategoryDb(Category_name=cat_name)
        obj.save()

    return redirect(add_category)

def display_category(request):
    category = AddcategoryDb.objects.all()
    return render(request,"display_category.html",{"category":category})

def edit_category(request,cat_id):
    category = AddcategoryDb.objects.get(id=cat_id)
    return render(request,"edit_category.html",{"category":category})

def update_category(request,cat_id):
    if request.method == "POST":
        cat_name = request.POST.get('category_name')
        AddcategoryDb.objects.filter(id=cat_id).update(Category_name=cat_name)
        return redirect(display_category)
    return redirect(display_category)

def delete_category(request,cat_id):
    data = AddcategoryDb.objects.filter(id=cat_id)
    data.delete()
    return redirect(display_category)

#**************************************************************************************

def contact_details(request):
    contact = ContactDb.objects.all()
    return render(request,"contact_details.html",{"contact":contact})

def delete_contact_details(request,con_id):
    data = ContactDb.objects.filter(id=con_id)
    data.delete()
    return redirect(contact_details)

#******************************************************************************************

def Issue_details(request):
    issues = IssueDb.objects.all()
    return render(request,"issue_details.html",{"issues":issues})

def delete_issue(request,issue_id):
    data = IssueDb.objects.filter(id=issue_id)
    data.delete()
    return redirect(Issue_details)

def update_issue_status(request, issue_id):
    if request.method == "POST":
        status = request.POST.get("status")
        if status in {
            IssueDb.STATUS_UNSOLVED,
            IssueDb.STATUS_IN_PROGRESS,
            IssueDb.STATUS_SOLVED,
        }:
            IssueDb.objects.filter(id=issue_id).update(Status=status)
    return redirect(Issue_details)


def comment_details(request):
    comments = CommentDb.objects.all()
    return render(request,"comment_details.html",{"comments":comments})

def delete_comment(request,com_id):
    data = CommentDb.objects.filter(id=com_id)
    data.delete()
    return redirect(comment_details)
