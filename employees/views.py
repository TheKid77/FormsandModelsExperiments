from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Employee
from .forms import AddEmployee
from django.shortcuts import render, redirect

def add_employee(request):
    """ Add a Book """

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = AddEmployee()
    else:
        # Post data submitted, process data
        form = AddEmployee(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('/employees/add_employee')
    # Display a blank or invalid form
    context = {'form': form}
    # template_name = 'books/new_book.html'
    return render(request, 'employees/add_employee.html', context)
