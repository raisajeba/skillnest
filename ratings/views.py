from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import RatingForm
from .models import Rating

def ratings_home(request):

    users = User.objects.exclude(
        id=request.user.id
    )

    return render(
        request,
        'ratings/home.html',
        {
            'users': users
        }
    )


@login_required
def give_rating(request, user_id):

    rated_user = get_object_or_404(
        User,
        id=user_id
    )

    if request.method == 'POST':

        form = RatingForm(
            request.POST
        )

        if form.is_valid():

            rating = form.save(
                commit=False
            )

            rating.reviewer = request.user
            rating.rated_user = rated_user

            rating.save()

            return redirect(
                'profile'
            )

    else:

        form = RatingForm()

    return render(
        request,
        'ratings/rate.html',
        {
            'form': form,
            'rated_user': rated_user
        }
    )
