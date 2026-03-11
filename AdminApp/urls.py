from django.urls import  path
from AdminApp import  views



urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('AdminLoginPage/',views.admin_login_page,name="AdminLoginPage"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('add_category/',views.add_category,name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:cat_id>',views.edit_category,name="edit_category"),
    path('update_category/<int:cat_id>',views.update_category,name="update_category"),
    path('delete_category/<int:cat_id>',views.delete_category,name="delete_category"),

    path('contact_details/',views.contact_details,name="contact_details"),
    path('delete_contact_details/<int:con_id>',views.delete_contact_details,name="delete_contact_details"),

    path('issue_details/',views.Issue_details,name="issue_details"),
    path('delete_issue/<int:issue_id>',views.delete_issue,name="delete_issue"),
    path('update_issue_status/<int:issue_id>',views.update_issue_status,name="update_issue_status"),
    path('comment_details/',views.comment_details,name="comment_details"),
    path('delete_comment/<int:com_id>',views.delete_comment,name="delete_comment")
]
