from django.shortcuts import render
from .models import Payment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Paymenthomeview(ListView):
    model = Payment
    template_name = 'payment/paymenthome.html'
    context_object_name = 'payments'


class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment/paymentdetails.html'
    context_object_name = 'payment'


class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    template_name = 'payment/payment_form.html'
    fields = ['patient_name', 'Total_amount', 'Deposit', 'Insurance',
              'collection_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PaymentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Payment
    template_name = 'payment/payment_form.html'
    fields = ['patient_name', 'Total_amount', 'Deposit', 'Insurance',
              'collection_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        payment = self.get_object()
        if self.request.user == payment.author:
            return True
        else:
            return False


class PaymentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Payment
    template_name = 'payment/payment_confirm_delete.html'
    context_object_name = 'payment'
    success_url = '/'

    def test_func(self):
        payment = self.get_object()
        if self.request.user == payment.author:
            return True
        else:
            return False
