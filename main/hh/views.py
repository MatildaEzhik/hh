
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from hh.forms import ResumeForm
from hh.models import Vacancy, Resume


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'hh/vacancy_list.html', {'vacancies': vacancies})

def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    return render(request, 'hh/vacancy_detail.html', {'vacancy': vacancy})

def resume_create(request, vacancy_id):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('vacancy_detail', id=vacancy_id)
    else:
        form = ResumeForm()
    return render(request, 'hh/resume_form.html', {'form': form})
