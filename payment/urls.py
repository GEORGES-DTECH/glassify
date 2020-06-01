from django.urls import path
from . import views
from .views import (
     Paymenthomeview,
     PaymentDetailView,
     PaymentUpdateView,
     PaymentCreateView,
     PaymentDeleteView)



urlpatterns = [
    path('', Paymenthomeview.as_view(), name='payment_home'),

    path('payment/new', PaymentCreateView.as_view(), name='payment_create'),
  
    path('payment/<int:pk>/', PaymentDetailView.as_view(), name='payment_details'),
    path('payment/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment_update'),
    path('payment/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment_delete'),
       



]
