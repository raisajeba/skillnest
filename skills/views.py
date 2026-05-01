from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Skill
from .forms import SkillForm,SkillImageFormSet


# home page
def index(request):
    all_skills = Skill.objects.all().order_by('-created_at')
    return render(request, 'skills/index.html', {'skills': all_skills})


#  skill details
def skill_detail(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    return render(request, 'skills/detailskill.html', {'skill': skill})


# skill add
@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        formset = SkillImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()

            formset.instance = skill
            formset.save()

            return redirect('index')
    else:
        form = SkillForm()
        formset = SkillImageFormSet()


    return render(request, 'skills/skillform.html', {'form': form,'formset':formset})


# skill update
@login_required
def update_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        formset = SkillImageFormSet(request.POST, request.FILES, instance=skill)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('skill_detail', pk=pk)
    else:
        form = SkillForm(instance=skill)
        formset = SkillImageFormSet(instance=skill)

    return render(request, 'skills/skillform.html', {
        'form': form,
        'formset': formset
    })

# skill delete
@login_required
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)

    if request.method == 'POST':
        skill.delete()
        return redirect('index')

    return render(request, 'skills/deleteconfirm.html', {'skill': skill})