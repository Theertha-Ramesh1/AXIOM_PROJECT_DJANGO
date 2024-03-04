from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='Engineer_index'),
    path('Engineer_login', views.engineerlogin, name='Engineer_login'),
    path('Engineer_signup/', views.engineersignupp, name='Engineer_signup'),
    path('Engineer_home/', views.home, name='Engineer_home'),
    path('addproject/', views.addproject, name='Add_project'),
    path('engi_projectview/', views.engi_projectview, name='engi_projectview'),
    path('addprojectimage/<int:id>',views.addprojectimage, name='addprojectimage'),
    path('projectdelete/<int:id>',views.engineerprojectdelete, name='engineerprojectdelete'),
    path('enquiry/',views.enuiryview, name='enquiry'),
    path('enquirydelete/<int:id>',views.engineerenuirydelete, name='enquirydelete'),
    path('eng_userview/', views.eng_userview, name='Engineer_userview'),
    path('eng_userblock/<int:id>', views.eng_userblock, name='eng_userblock'),
    path('eng_userunblk/<int:id>', views.eng_userunblk, name='eng_userunblk'),
    path('eng_userdelete/<int:id>', views.eng_userdelete, name='eng_userdelete'),
    path('logout/', views.engineerlogout, name='engineerlogout'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)