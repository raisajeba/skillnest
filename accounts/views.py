from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from skills.models import Skill

from .forms import SkillForm, ProfileForm


def signup(request):

    form = UserCreationForm()

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')


    return render(
        request,
        'accounts/signup.html',
        {'form': form}
    )



@login_required
def profile(request):

    skills = Skill.objects.filter(
        user=request.user
    )


    return render(
        request,
        'accounts/profile.html',
        {
            'skills': skills
        }
    )



# PROFILE EDIT
@login_required
def edit_profile(request):

    profile = request.user.profile


    form = ProfileForm(

        request.POST or None,
        request.FILES or None,

        instance=profile
    )


    if form.is_valid():

        form.save()

        return redirect('profile')


    return render(
        request,
        'accounts/edit_profile.html',
        {
            'form': form
        }
    )



# ADD SKILL
@login_required
def add_skill(request):

    form = SkillForm(

        request.POST or None,
        request.FILES or None
    )


    if form.is_valid():

        skill = form.save(
            commit=False
        )

        skill.user = request.user

        skill.save()

        return redirect('profile')


    return render(
        request,
        'accounts/skill_form.html',
        {
            'form': form
        }
    )



# EDIT SKILL
@login_required
def edit_skill(request, pk):

    skill = get_object_or_404(

        Skill,

        pk=pk,

        user=request.user
    )


    form = SkillForm(

        request.POST or None,

        request.FILES or None,

        instance=skill
    )


    if form.is_valid():

        form.save()

        return redirect('profile')


    return render(
        request,
        'accounts/skill_form.html',
        {
            'form': form
        }
    )



# DELETE SKILL
@login_required
def delete_skill(request, pk):

    skill = get_object_or_404(

        Skill,

        pk=pk,

        user=request.user
    )


    if request.method == "POST":

        skill.delete()

        return redirect('profile')


    return render(
        request,
        'accounts/delete_skill.html',
        {
            'skill': skill
        }
    )