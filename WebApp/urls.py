from django.urls import path
from WebApp import views

urlpatterns = [

    path('sign_in/',views.sign_in,name="sign_in"),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('save_user/',views.save_user,name="save_user"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),

    path('home/',views.home_page,name="home"),
    path('all_post/',views.all_post,name="all_post"),

    path('save_contact/',views.save_contact,name="save_contact"),
    
    path('report_issue/',views.report_issue,name="report_issue"),
    path('save_issue/',views.save_issue,name="save_issue"),
    path('save_comments/',views.save_comments,name="save_comments"),

    path('view_details/<int:issue_id>',views.view_details,name="view_details")

]