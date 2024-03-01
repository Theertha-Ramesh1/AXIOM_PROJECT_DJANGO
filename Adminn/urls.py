from django.urls import path
from Adminn import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.admin_login, name='adminlogin'),
    path('axiomadmin/',views.axiom_admin, name='adminhome'),
    path('adminlogout', views.admin_logout, name='adminlogout'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('admincategoryview', views.admincategory_view, name='categoryview'),
    path('categorydelete/<int:id>', views.categorydelete, name='categorydelete'),
    path('userview',views.userview,name='userview'),
    path('userblock/<int:id>', views.userblock, name='userblock'),
    path('userunblk/<int:id>', views.userunblk, name='userunblk'),
    path('engineerblock/<int:id>', views.engineerblock, name='engineerblock'),
    path('engineerunblk/<int:id>', views.engineerunblk, name='engineerunblk'),
    path('userdelete/<int:id>',views.userdelete, name='userdelete'),
    path('engineerview', views.engineerview,name='engineerview'),
    path('engineerdelete/<int:id>', views.engineerdelete, name='engineerdelete'),
    path('engineerrequest', views.engineerrequest, name='engineerrequest'),
    path('engineerapprove/<int:id>', views.engineerapprove,name='engineerapprove'),
    path('projectview',views.adminprojectview,name='projectview'),
    path('projectdelete/<int:id>',views.adminprojectdelete,name='projectdelete'),
    path('enquiry_view/', views.enquiry_view, name='enquiry_view'),
    path('enquiry_delete/<int:id>', views.enquiry_delete, name='enquiry_delete'),

    # path('enquiry/', views.enquiry, name='enquiry'),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)