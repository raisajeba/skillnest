from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ExchangeRequest
from accounts.models import Profile
from skills.models import Skill
# send request
@login_required
def send_request(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)

    ExchangeRequest.objects.create(
        sender=request.user,
        receiver=skill.user,
        skill=skill
    )

    return redirect('exchange_home')

@login_required
def exchange_home(request):
    inbox = ExchangeRequest.objects.filter(receiver=request.user)
    sent = ExchangeRequest.objects.filter(sender=request.user)

    return render(request, 'exchanges/inbox.html', {
        'inbox': inbox,
        'sent': sent
    })
@login_required
def request_action(request, pk, action):
    exchange = get_object_or_404(
        ExchangeRequest,
        id=pk,
        receiver=request.user,
        status='pending'
    )

    if action == "accept":
        exchange.status = "accepted"

        profile = Profile.objects.get(user=request.user)
        profile.points += 20
        profile.save()

    elif action == "reject":
        exchange.status = "rejected"

    exchange.save()
    return redirect('exchange_home')

@login_required
def delete_request(request, pk):
    exchange = get_object_or_404(
        ExchangeRequest,
        id=pk,
        sender=request.user
    )

    if request.method == "POST":
        exchange.delete()

    return redirect('exchange_home')

