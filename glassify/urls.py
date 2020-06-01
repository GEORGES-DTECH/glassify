from django.contrib import admin
from django.urls import path, include

from patients.views import Patienthomeview

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Patienthomeview.as_view(), name='patient_home'),
  
    path('accounts/', include('accounts.urls')),
    path('patients/', include('patients.urls')),
    path('payment/', include('payment.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

