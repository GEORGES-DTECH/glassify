from django.shortcuts import render
from .models import Patient
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Patienthomeview(ListView):
    model = Patient
    template_name = 'patients/patientshome.html'
    context_object_name = 'patients'
    paginate_by=30


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/patientsdetails.html'
    context_object_name = 'patient'


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = 'patients/patients_form.html'
    fields = ['Date', 'patients_name', 'patients_mobile', 'patients_age',
              'Right_eye', 'Left_eye', 'frame', 'lenses']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    template_name = 'patients/patients_form.html'
    fields = ['Date', 'patients_name', 'patients_mobile', 'patients_age',
              'Right_eye', 'Left_eye', 'frame', 'lenses']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.author:
            return True
        else:
            return False


class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Patient
    template_name = 'patients/patients_confirm_delete.html'
    context_object_name = 'patient'
    success_url = '/'

    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.author:
            return True
        else:
            return False
