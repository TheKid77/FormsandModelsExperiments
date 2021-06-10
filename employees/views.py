from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Employee
from .forms import AddEmployee, AddAnnualReview
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

def add_employee(request):
    """ Add an Employee """

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = AddEmployee()
    else:
        # Post data submitted, process data
        form = AddEmployee(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('/employees')
    # Display a blank or invalid form
    context = {'form': form}
    # template_name = 'books/new_book.html'
    return render(request, 'employees/add_employee.html', context)

def add_annual_review(request):
    """ Add an Annual Review """

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = AddAnnualReview()
    else:
        # Post data submitted, process data
        form = AddAnnualReview(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('/employees')
    # Display a blank or invalid form
    context = {'form': form}
    # template_name = 'books/new_book.html'
    return render(request, 'employees/add_annual_review.html', context)