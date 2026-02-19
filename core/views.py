from django.shortcuts import render, redirect
from .forms import AssignmentForm

def home(request):
    username = request.COOKIES.get('username')

    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            # ❌ Do NOT save to database on Vercel
            student_name = form.cleaned_data.get('student_name')

            response = redirect('/')
            response.set_cookie('username', student_name)
            return response
    else:
        form = AssignmentForm()

    # ❌ Disable database usage
    assignments = []

    return render(request, 'home.html', {
        'form': form,
        'assignments': assignments,
        'username': username
    })
