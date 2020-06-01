from django.urls import path
from . import views
from .views import (
     Patienthomeview,
     PatientDetailView,
     PatientUpdateView,
     PatientCreateView,
     PatientDeleteView)



urlpatterns = [
    path('', Patienthomeview.as_view(), name='patient_home'),

    path('patient/new', PatientCreateView.as_view(), name='patient_create'),
  
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient_details'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient_update'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
       



]
