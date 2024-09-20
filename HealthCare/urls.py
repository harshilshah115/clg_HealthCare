from django.urls import path
import HealthCare.views as view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', view.submit_register, name='register'),
    path('login/', view.submit_login, name='login'),
    path('home/', view.submit_home, name='home'),
    path('profile/', view.submit_profile, name='profile'),
    path('profileup/', view.submit_update_profile, name='updateprofile'),
    path('upload_report/', view.upload_report, name='upload_report'),
    path('medicen/', view.medicen, name='medicen'),
    path('ordermedicen/', view.ordermedicine, name='ordermedicine'),
    path('submitappoinment',view.submit_appoinment,name='submitappoinment'),
    path('appoinment/', view.appoinment, name='appoinment'),
    path('login/', view.submit_logout, name='logout'),
]


#Use for Media file upload logic
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
