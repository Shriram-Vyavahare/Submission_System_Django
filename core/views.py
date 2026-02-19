
from django.shortcuts import render, redirect
from .forms import AssignmentForm
from .models import Assignment

def home(request):
    username = request.COOKIES.get('username')

    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save()
            response = redirect('/')
            response.set_cookie('username', assignment.student_name)
            return response
    else:
        form = AssignmentForm()

    assignments = Assignment.objects.all().order_by('-submitted_at')

    return render(request, 'home.html', {
        'form': form,
        'assignments': assignments,
        'username': username
    })
