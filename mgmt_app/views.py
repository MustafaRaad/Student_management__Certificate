from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from mgmt_app.forms import StudentForm
from django.urls import reverse
from mgmt_app.models import Student


# ------------------------------Students-----------------------------------


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    paginate_by = 100
    context_object_name = 'student'
    template_name = 'students/student_list.html'
    login_url = 'login'


class StudentCertView(LoginRequiredMixin, DetailView):
    model = Student
    context_object_name = 'student'
    template_name = "students/student_cert.html"
    slug_field = 'id'
    login_url = 'login'


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student

    context_object_name = 'student'
    template_name = "students/student_detail.html"
    slug_field = 'id'
    login_url = 'login'


class StudentCreateView(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = StudentForm
    template_name = "students/student_create.html"
    queryset = Student.objects.all()
    permission_required = 'mgmt_app.add_student'
    success_message = "Created successfully"

    def form_valid(self, form):
        return super().form_valid(form)


class StudentUpdateView(PermissionRequiredMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = 'login'
    form_class = StudentForm
    template_name = "students/student_update.html"
    queryset = Student.objects.all()
    context_object_name = 'student'
    permission_required = 'mgmt_app.add_student'
    success_message = "%(first_name)s was updated successfully"

    # success_url = '/success/'

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = None
        if pk is not None:
            obj = get_object_or_404(Student, pk=pk)
        return obj

    def form_valid(self, form):
        return super().form_valid(form)


class StudentDeleteView(SuccessMessageMixin,LoginRequiredMixin, DeleteView):
    login_url = 'login'
    template_name = "students/student_delete.html"
    queryset = Student.objects.all()
    success_message = "Student Deleted successfully"

    def get_success_url(self):
        return reverse('student:student-list')
    

"""
##########################################
##  Developed By:Mustafa Raad Mutashar  ##
##  mustafa.raad.7@gmail.com     2020   ##
##########################################
"""
