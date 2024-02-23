from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('editprofile',views.profileedit,name="editprofile"),
    path('home/', views.home, name='home'),
    path('engineers/', views.engineers,name='engineers'),
    path('project/', views.project, name='project'),
    path('individualproject/<int:id>', views.individualproject, name='individualproject'),
    path('individualprofile/<int:id>', views.individualprofile, name='individualprofile'),
    path('individualproject/reviewadd/<int:id>', views.reviewadd, name='reviewadd'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('plans/', views.plans, name='plans'),
    path('enquiry/', views.enquiry, name='enquiry'),
    # path('get_engineers/', views.get_engineers, name='get_engineers'),
    path('logout/', views.logout, name='logout'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)