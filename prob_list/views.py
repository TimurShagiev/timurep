from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProblemForm
from .models import Problem
from .forms import ProblemUpdateForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group


@login_required
def problem_list(request):
    problems = Problem.objects.filter(assigned_user=request.user, status__in=['new', 'in_progress', 'confirmed'])
    return render(request, 'prob_list/problem_list.html', {'problems': problems})


@login_required
def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)

    if request.method == 'POST':
        form = ProblemUpdateForm(request.POST, instance=problem)
        if form.is_valid():
            updated_problem = form.save(commit=False)
            if updated_problem.status == 'resolved':
                updated_problem.resolved_user = request.user
                reception_group = Group.objects.get(name='Reception')
                users_in_reception = reception_group.user_set.all()
                if users_in_reception:
                    updated_problem.assigned_user = users_in_reception[0]
            updated_problem.save()
            return redirect('problem_list')
    else:
        form = ProblemUpdateForm(instance=problem)

    return render(request, 'prob_list/problem_detail.html', {'problem': problem, 'form': form})


def new_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            reception_group = Group.objects.get(name='Reception')
            users_in_reception = reception_group.user_set.all()
            if users_in_reception:
                problem.assigned_user = users_in_reception.first()
            problem.user = request.user
            problem.save()
            return redirect('problem_list')
    else:
        form = ProblemForm()
    return render(request, 'prob_list/new_problem.html', {'form': form})

def about(request):
    return render(request, 'prob_list/about.html')


